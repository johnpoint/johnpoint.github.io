---
title: deepin 应用字体异常解决方法
author: johnpoint
date: 2019-10-12 23:30:37
tags:
- deepin
- 字体
- 折腾
---

写下我是怎么解决 deepin 应用字体异常的<!--more-->

linux 在国内推广的难度，我想大多数来自于国内的某些大公司在用户端对于 linux(不包含 android) 系统的不友好。

deepin 这家公司就做了许多移植软件，比如 Foxmail、TIM，尽管他们都是运行在定制的 wine 中的，但也算是能用了，美中不足的是，deepin-wine 的 windows 环境之中似乎没有字体文件，所以会造成软件界面的字体渲染出错。

解决方法嘛，我从 win10 虚拟机里面把字体提取出来并做了个软链接(节省空间)到容器的字体文件夹(`~/.deepinwine/Deepin-Foxmail/drive_c/windows/Fonts`)就好了。