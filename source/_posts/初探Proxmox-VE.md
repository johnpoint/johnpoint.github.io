---
title: 初探 Proxmox VE
author: johnpoint
date: 2019-03-17 11:36
toc: true
tags:
- Proxmox VE
---

一直好奇主机商们是怎么把一台独立服务器分成 VPS 来售卖的，这几天就去玩了 下 Proxmox VE
<!--more-->
![](https://cdn.lvcshu.info/img/20190317001.jpg)

# 环境

- Ubuntu 18.04.2 桌面版
- VirtualBox Graphical User Interface Version 5.2.18_Ubuntu r123745
- Proxmox-ve_5.3-2

# 安装


由于我手头上实在是没有空余的机器，所以我向我的笔记本 ~~伸出了邪恶的手~~ ，新建了一个虚拟机，分配给它 4G 内存， 50G 硬盘 。安装时候直接在 [官网-下载](https://www.proxmox.com/en/downloads) 下载 `Proxmox VE 5.3 ISO Installer` iso 镜像，像平时安装系统一样安装上去，完全傻瓜式。


安装好以后就会提示你登录并给了你一个网页的地址，就像这样

![](https://cdn.lvcshu.info/img/20190317002.png)

但是我们的是虚拟机所以需要在 `Settings->Network->Adapter 1->Advanced->Port Forwarding` 配置端口转发

然后在浏览器访问 `https://127.0.0.1:映射的端口` 就可以看见面板了。

![](https://cdn.lvcshu.info/img/20190317003.png)

# 使用


面板的右上角有 `[创建虚拟机]` `[创建 CT]` 的按钮，分别对应虚拟化技术 KVM 以及 OpenVZ（LXC？）

## 镜像下载

### KVM

直接下载官方的安装镜像，并把镜像放置在  

`/var/lib/vz/template/iso`

### OpenVZ

需要到 OpenVZ 官网的 [下载页面](https://wiki.openvz.org/Download/template/precreated) 下载

放置目录是

`/var/lib/vz/template/cache`

## 网卡 & NAT

由于我是虚拟机开虚拟机，并且没有公网ip，所以我们需要通过 NAT(**N**etwork **A**ddress **T**ranslation)来对流量转发，~~不然就是单机游戏啦~~

## 母鸡的配置

编辑文件 `/etc/network/interfaces` 添加

```
auto vmbr2
iface vmbr4 inet static
        address  10.97.0.254
        netmask  255.255.255.0
        bridge-ports none
        bridge-stp off
        bridge-fd 0
        post-up echo 1 > /proc/sys/net/ipv4/ip_forward
        post-up iptables -t nat -A POSTROUTING -s '10.97.0.0/24' -o vmbr0 -j MASQUERADE
        post-down iptables -t nat -D POSTROUTING -s '10.97.0.0/24' -o vmbr0 -j MASQUERADE
        post-up iptables -t nat -A PREROUTING -i vmbr0 -p tcp --dport 1024 -j DNAT --to 10.97.0.1:22
        post-down iptables -t nat -D PREROUTING -i vmbr0 -p tcp --dport 1024 -j DNAT --to 10.97.0.1:22
```

然后执行 `/etc/init.d/networking restart`

就能添加一张网卡，这张网卡主要是用于接下来的小鸡的流量转发用的，他会把所有的流量转向母鸡可以连接外网的网卡。

## 小鸡的配置

![](https://cdn.lvcshu.info/img/20190317004.png)

按照上面的信息随机应变 (?) 就好，网管要填 **母鸡的IP**

# Tips:
- 这里的配置主要是开 CT 容器，KVM 的或许以后会更 ~~咕咕咕~~
- centos 7 的 OpenVZ 镜像貌似有问题，密码是没有办法输对的

# 最后

开了三台服务器～

![](https://cdn.lvcshu.info/img/20190317005.png)

# 参考

- [Proxmox VE三种方法配置NAT小鸡和IPv6地址](https://www.imfan.net/geek/20.html)
- [Proxmox VE安装和KVM开设教程](http://www.zrblog.net/16527.html)
- [OpenVZ安装指南](https://teddysun.com/296.html)



