---
title: <失效> Ubuntu 安装 thinkpad S2 无线网卡驱动
author: johnpoint
date: 2018-08-25 16:58
tags:
- Ubuntu
- thinkpad S2
---

**注意：本文已失效，目前有效的方法在 [这里](/2019/06/06/Ubuntu安装rtl8821ce驱动/)**

最近入手了一台 thinkpad S2 ，打开 windows 系统，觉得缺了点什么，于是连忙把 ubuntu 系统也安装了上去，但是在配置 ubuntu 系统的时候并没有让我连接网络的选项，当时就感觉有些奇怪<!---more--->，但是没有放在心上。安装完成后打开 *ubuntu* 系统发现系统 **根本没有** 检测到无线网卡的存在，于是我就慌了，赶紧回到 *windows* 系统，看见了无线网卡的型号
```
Realtek 8821CE Wireless LAN 802.11ac PCI-E NIC
```
于是使用强大的 ~~百度~~ **google** 搜索解决办法，最后在 ubuntu论坛 的[这个帖子](http://forum.ubuntu.org.cn/viewtopic.php?f=116&t=485936)里发现了解决办法。

# 解决方法
由[这个帖子里](http://forum.ubuntu.org.cn/viewtopic.php?f=116&t=485936)的大佬在[这里](https://unix.stackexchange.com/questions/379049/realtek-wifi-driver-problem-in-linux-mint-18-2)请教到的大佬给出解决方法

原文如下：
```
Worked solution (Requirements: kernel >=4.11) :

(UPD: In the latest release of endlessm you need kernel version 4.15)

Download driver directory from this repo: https://github.com/endlessm/linux/tree/master/drivers/net/wireless/rtl8821ce
You can do it by this link: https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/endlessm/linux/tree/master/drivers/net/wireless/rtl8821ce

Unpack zip archive.
Change the Makefile. Line "export TopDIR ?= ..." to export "TopDIR ?= PATH TO EXTRACTED DIRECTORY".


$ make
$ sudo make install
$ sudo modprobe -a 8821ce
```
至此，完美解决了这个问题

# 一点小问题
在某次 ubuntu 的内核升级了以后，我发现我的无线网卡驱动 **又没了** ~~马上扔掉电脑~~ 于是我想到了使用脚本进行安装，这样就可以在下一次遇到这样的问题时快速解决！

脚本内容：
```
#!/bin/bash

mv rtl8821ce.zip /home/johnpoint
cd ~
unzip rtl8821ce.zip
cd rtl8821ce
make
sudo make install
sudo modprobe -a 8821ce

exit 0
```
撒花
