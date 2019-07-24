---
title: Linux 家族:Alpine 体验
date: 2019-07-24 17:16:00
toc: true
tags:
- Alpine
- Linux
- 折腾
---

最近心痒痒想折腾下新的系统，顺便记录一下。<!--more-->

# 介绍

Alpine Linux是一个由社区开发的Linux操作系统，该操作系统以安全为理念，面向x86路由器、防火墙、虚拟专用网、IP电话盒及服务器而设计。
<sub>摘自[维基百科](https://zh.wikipedia.org/wiki/Alpine_Linux)</sub>

![官网图](https://cdn.lvcshu.info/img/20190724001.png)

我是怎么发现这个系统的呢，前一阵子我在折腾 Docker 的时候我就发现 nginx 的官方 docker 仓库里面有一些 tag 的大小有很大的区别

![](https://cdn.lvcshu.info/img/20190724002.png)

所以我就去 Google 了一下 alpine 的含义，就发现了这样的一个精简的 Linux 系统。

# 安装

安装体验 ★★★★

在官网下载 STANDARD 镜像大小仅 112 MB，可以说是特别小了，我去隔壁看一下 Arch 哇，比 Arch 的安装镜像（615 MB）还要小诶。

安装过程简单明了。

![进入安装界面有安装系统的提示](https://cdn.lvcshu.info/img/20190724003.png)

![选择键盘布局 & 配置网络](https://cdn.lvcshu.info/img/20190724004.png)

![配置](https://cdn.lvcshu.info/img/20190724005.png)

![配置硬盘 & 写入系统](https://cdn.lvcshu.info/img/20190724006.png)

然后经过等待就搞定系统的安装了，虽然没有 GUI 但是安装体验还是挺好的。

# 使用

## 包管理

alpine 使用的包管理器叫做 apk，查询有无相应的包可以使用 [Alpine Linux Packages](https://pkgs.alpinelinux.org/packages) 进行查询。

![](https://cdn.lvcshu.info/img/20190724007.png)

当然也可以使用 apk 的 `apk search` 命令进行查询。

## 修改国内镜像源

我使用 tuna 的源

修改 `/etc/apk/repositories`

```
https://mirrors.ustc.edu.cn/alpine/v3.10/main
https://mirrors.ustc.edu.cn/alpine/v3.10/community
https://mirrors.ustc.edu.cn/alpine/edge/main
https://mirrors.ustc.edu.cn/alpine/edge/community
https://mirrors.ustc.edu.cn/alpine/edge/testing
```

## 修改 SSH 设置

alpine 默认的 ssh 设置是不能远程链接的。。。

修改 `/etc/ssh/sshd_config`

添加 `PermitRootLogin yes` 即可

差不多就写到这~