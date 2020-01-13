---
title: Archlinux 系统体验报告
date: 2020-01-13 22:16:00
toc: true
tags:
- Arch
- 体验
pressone: https://press.one/file/v?s=578f6c338bbdc0f9bee8a948a900da87597b54e4c340f30e6c46a54d83d27a31180fc70ee8e7966a1a302b423fcc36eee54aad0a7aff897daa28d494711f32d200&h=9cfe07deb55fa1ef3f85f9314d9d98e3f88a3c5217e9b308fd13777940e68ab7&a=79a3a060a7faa9dfc9b8b4e0a59bf3ebac305f78&f=P1&v=3
---
<!--more-->
```
                   -`                    johnpoint@archlinux 
                  .o+`                   ------------------- 
                 `ooo/                   OS: Arch Linux x86_64 
                `+oooo:                  Host: ××××××××××××
               `+oooooo:                 Kernel: 5.4.8-arch1-1 
               -+oooooo+:                Uptime: 18 hours, 43 mins 
             `/:-:++oooo+:               Packages: 1389 (pacman) 
            `/++++/+++++++:              Shell: zsh 5.7.1 
           `/++++++++++++++:             Resolution: 1920x1080, 1920x1080 
          `/+++ooooooooooooo/`           DE: Plasma 
         ./ooosssso++osssssso+`          WM: KWin 
        .oossssso-````/ossssss+`         Theme: Breeze [GTK2/3] 
       -osssssso.      :ssssssso.        Icons: breeze [GTK2/3] 
      :osssssss/        osssso+++.       Terminal: konsole 
     /ossssssss/        +ssssooo/-       Terminal Font: Cascadia Code 11 
   `/ossssso+/:-        -:/+osssso+-     CPU: Intel i5-8250U (8) @ 3.400GHz 
  `+sso+:-`                 `.-/+oso:    GPU: Intel UHD Graphics 620 
 `++:.                           `-/+/   Memory: ××××××××××××
 .`                                 `/
```

今天写一下在这段时间 Archlinux 的使用体验。

从去年上半年开始我先是使用的 Ubuntu 18.04 作为我的笔记本电脑兼主用电脑使用，Ubuntu 的桌面版本的使用体验其实已经不逊于 Windows 系统（除了 office 套件还是 Windows 上好用），开源的 office 套件方案（Libreoffice）也已经相对成熟也可以在大部分时间下代替 MS office 存在。

前些时候，我也写过一篇 Archlinux 的安装指南（[传送门](https://blog.lvcshu.com/2019/05/07/安装Arch笔记/)），但是那时候我是在虚拟机里面安装的，主要是怕翻车（逃

在 2019 年下半年，我才在 Yuuta 的一条[频道消息](https://t.me/c/1076844146/10385)的提醒下想起了那被我遗忘的 Archlinux 遂备份文件准备把主用的系统换过去。

# 使用体验

- 桌面环境: 纯净的 KDE 体验，在我这里没有出现啥奇怪的问题
- 网页浏览: 选用了 Chromium，体验与其他平台的 Chrome 基本一致
- 视频: VLC 我觉得是最好用的播放器
- 文档编辑: Libreoffice 体验一般，就是能用的程度
- 代码: 
    - VScode 跨平台体验一致
    - Netbean 跨平台体验一致
- 视频编辑: 无此需求
- 游戏:
    - Steam 我 想/能 玩的游戏都运行正常(缺氧 && 异星工厂)
    - Minecraft Java 跨平台
    
# 坑

- 内核升级的时候 wifi 的内核驱动模块不能自己挂载，往往需要自己重新加载
- 由于内核版本太高，有一次编译出来的 go 可执行文件放到了服务器上时提示 glibc 版本不存在