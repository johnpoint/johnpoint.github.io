---
title: Ubuntu 安装 rtl8821ce 驱动
author: johnpoint
date: 2019-06-06 21:51:00
toc: true
tags:
- ubuntu
- rtl8821ce
---

~~电脑又出问题了~~<!--more-->

升级了 ubuntu 19.04 以后我发现因为内核的更新，[之前的驱动安装方法](/2018/08/25/Ubuntu安装-thinkpad-S2-无线网卡驱动/) 已经失效了，所以就去寻找了新的安装方法

# 感谢

- [tomaspinho/rtl8821ce](https://github.com/tomaspinho/rtl8821ce)

# 安装

```
sudo apt install dkms git -y
git clone https://github.com/tomaspinho/rtl8821ce
cd rtl8821ce
```

**注意：之后就要断网，我是直接关掉了网络服务**

```
./dkms-install.sh
```
完成后加载模块
```
sudo modprobe 8821ce
```

完成撒花～


