https://grafana.com/blog/2021/02/09/how-i-monitor-my-openwrt-router-with-grafana-cloud-and-prometheus/

---
title: 使用 headscale 异地组网
author: johnpoint
date: 2022-11-04 10:00:00
tags:
- 笔记
toc: true
---

很久之前看过柠檬大佬的[使用 N2N 进行异地组网的文章](https://blog.ilemonrain.com/linux/n2n-v2-tutorial.html)，大受震撼，但是 N2N 的部署体验很难说得上令人愉悦。

然后就听说了 wireguard 被加入 linux 内核，以下是 wireguard 的介绍：

> **WireGuard**是由Jason A. Donenfeld开发的[开放源代码](https://zh.wikipedia.org/wiki/%E5%BC%80%E6%94%BE%E6%BA%90%E4%BB%A3%E7%A0%81)[VPN](https://zh.wikipedia.org/wiki/%E8%99%9B%E6%93%AC%E7%A7%81%E4%BA%BA%E7%B6%B2%E8%B7%AF)程序及协议[[1]](https://zh.wikipedia.org/wiki/WireGuard#cite_note-wireguard-site-1)，基于[Linux内核](https://zh.wikipedia.org/wiki/Linux%E5%86%85%E6%A0%B8)实现，利用[Curve25519](https://zh.wikipedia.org/wiki/Curve25519)进行密钥交换，[ChaCha20](https://zh.wikipedia.org/wiki/ChaCha20 "ChaCha20")用于加密，[Poly1305](https://zh.wikipedia.org/wiki/Poly1305 "Poly1305")用于数据认证，[BLAKE2](https://zh.wikipedia.org/wiki/BLAKE2 "BLAKE2")用于[散列函数](https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8 "散列函数")运算[[1]](https://zh.wikipedia.org/wiki/WireGuard#cite_note-wireguard-site-1)，支持[IPv4](https://zh.wikipedia.org/wiki/IPv4 "IPv4")和[IPv6](https://zh.wikipedia.org/wiki/IPv6 "IPv6")的第3层。[[2]](https://zh.wikipedia.org/wiki/WireGuard#cite_note-wireguard-whitepaper_section1-2)WireGuard旨在获得比[IPsec](https://zh.wikipedia.org/wiki/IPsec "IPsec")和[OpenVPN](https://zh.wikipedia.org/wiki/OpenVPN "OpenVPN")更好的性能[[3]](https://zh.wikipedia.org/wiki/WireGuard#cite_note-3)。

确实，wireguard 性能十分不错，但是配置实在是过于繁琐了，如果要往 wireguard 网络中加入一台设备，则需要修改几乎所有连入网络设备的配置文件，实在是太麻烦了，好在现在已经有了 tailscale 这个服务提供商提供了基于 wireguard 的 0 配置的 VPN 组网方案。

而 headscale 就是 tailscale 中控服务端的开源版本，开源版本支持自己部署，同时没有连入设备的数量限制，于是我花了一点时间将 headscale 部署了一下。

## 使用到的项目

[Github:juanfont/headscale](https://github.com/juanfont/headscale)
[Github:gurucomputing/headscale-ui](https://github.com/gurucomputing/headscale-ui)

## 部署 headscale

这里我使用 docker-componse 进行部署

```yml
version: '3.5'
services:
  headscale:
    image: headscale/headscale:latest-alpine
    container_name: headscale
    volumes:
      - ./container-config:/etc/headscale
      - ./container-data/data:/var/lib/headscale
    ports:
      - 27896:8080
    command: headscale serve
    restart: unless-stopped
  headscale-ui:
    image: ghcr.io/gurucomputing/headscale-ui:latest
    restart: unless-stopped
    container_name: headscale-ui
    ports:
      - 9443:443
```

同时我还使用了nginx来进行反向代理，将 headscale-ui 和 headscale 分别部署在了不同的域名下面，因此要做一些 CORS 的处理，Nginx 配置文件参考如下

```conf
location / {
        add_header 'Access-Control-Allow-Origin' '{{UI的域名}}' always;
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS,DELETE ,PUT' always;
        add_header 'Access-Control-Allow-Headers' 'authorization ,DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range' always;
        add_header 'Access-Control-Expose-Headers' 'Content-Length,Content-Range' always;
        if ($request_method = 'OPTIONS') {
            add_header 'Access-Control-Allow-Origin' '{{UI的域名}}' always;
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS,DELETE ,PUT ' always;
            add_header 'Access-Control-Allow-Headers' 'authorization ,DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range' always;
            add_header 'Access-Control-Expose-Headers' 'Content-Length,Content-Range' always;
            add_header 'Access-Control-Max-Age' 1728000;
            add_header 'Content-Type' 'text/plain; charset=utf-8';
            add_header 'Content-Length' 0;
            return 204;
        }
        proxy_pass {{headscale的地址}};
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_redirect default;
    }
```

## 配置 headscale-ui

headscale-ui 这个项目是一个纯前端的项目，是通过用户的浏览器直接调用 headscale 的 API 接口，所以需要自己去 headscale container 内部创建 apikey 来通过鉴权

```shell
docker exec -it headscale headscale apikey create
```

这个指令会创建一个 apikey，将他填入 headscale-ui 的配置里面即可，这里的配置仅保留在本地，不会上传到任何地方，所以如果更换了设备或者浏览器想要进行 headscale 的配置的话，要将这一步重复一遍。

## 配置 ACL

headscale 同时还支持 ACL 功能，从而控制在这个大内网之中设备能访问的设备，这边我写了个比较简单的 ACL 配置文件

```json
// ./container-config/acl.json
{
    "groups": {
        "group:admin": ["admin"], // 管理员用户
        "group:user": ["user"], // 普通用户
    },
    "acls": [
        // { "action": "accept", "src": ["*"], "dst": ["*:*"] },
        { "action": "accept", "src": ["group:admin"], "dst": ["*:*"] }, // 管理员用户的设备能访问所有设备
        { "action": "accept", "src": ["group:user"], "dst": ["tag:share:*","autogroup:self:*"] }, // 普通用户仅能访问带 share 标签以及自己的设备
    ],
    "ssh": [
        {
            "action": "check",
            "src": [
                "autogroup:members"
            ],
            "dst": [
                "autogroup:self"
            ],
            "users": [
                "autogroup:nonroot",
                "root"
            ]
        },
    ],
    "tagOwners": {
        "tag:share": ["group:admin"],
    },
}
```

同时，要修改配置文件里面的 `acl_policy_path`
```ini
acl_policy_path: "/etc/headscale/acl.json"
```

这样基本上就大功告成了，客户端的配置网上基本上都有，就不多写了。