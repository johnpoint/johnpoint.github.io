---
title: Android Q 初体验
author: johnpoint
date: 2019-05-10 13:29:57
tags:
- Android
- 初体验
- 折腾
---

最近开的 Google I/O 大会公布了 Android Q beta3 的几款适配的机型，我的 Oneplus 6 恰好也在其中<!--more-->

开心!!

然后今天在刷入了 Android Q beta3 OOS 版后发现了不少的问题，毕竟 BETA 嘛，还不是正式版本，也可以理解，主要我能体验到的几点是:

- 通知栏图标太大了
- 快捷键 **只有** 三大金刚 说好的全面屏手势呢？
- 设置了 PIN 码以后如果重启手机的话是 **不能** 成功的通过验证的
- 指纹解锁是 **无效** 的
- SmartLock 内 **没有** 面部解锁
- Google Assistant **不能** 通过 'OK，google' 唤醒
- 通知采用的是右滑消除，左滑会有延迟提醒等更多的功能，行为模式需要一定的时间习惯
- 权限管理细致了许多
- 流畅度在我的体验里面没有特别的改变
- USB 传文件似乎会导致系统错误？？（遇到过一次没有严格证实
- 动画的渐变变得更好看了
- 似乎没有找到隐藏刘海的选项

# 笔记

记录下 adb 跳过手机开机设置向导的方法，实测有效!!

```
adb shell settings put secure user_setup_complete 1
adb shell settings put global device_provisioned 1
```

然后重启

>此方法来源于: [Android 跳过Gapps开机引导](https://www.jianshu.com/p/1776170650d5)