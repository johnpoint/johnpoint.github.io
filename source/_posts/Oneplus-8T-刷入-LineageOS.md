---
title: Oneplus 8T 刷入 LineageOS
author: johnpoint
date: 2022-05-01 11:51:00
tags:
- Android
- 自动构建
- 折腾
toc: true
---
劳动节来给博客除除草！

自从一加手机社区发布了[官方公告](https://www.oneplusbbs.com/thread-6275993-1.html)说 Android 12 正式版本出来了之后我就一直在等系统更新的推送，谁知道从4月12日公告出来到今天我都没有收到推送，再加上一加的在 Android 12 后 HOS 会切换成 ColorOS，类原生的特点就没有了，OOS 虽说还会持续维护，但是我既然都用 OOS 了我为啥不自己刷个更加原生的系统呢？比如说 LineageOS。

## 前期准备

说干就干，先去官网看下有没有支持，芜湖，[有支持](https://wiki.lineageos.org/devices/kebab/)而且看了下文档还蛮完善的，备份好微信(这个手机里面唯一没有同步功能的app)的数据就打算开始刷机了。

## 开刷
刷机的过程[官方文档](https://wiki.lineageos.org/devices/kebab/install)已经非常完善了，在这里不重复赘述。

## 一些要注意的小问题
### GAPPS
GAPPS 一定要在首次启动系统之前刷入，不然就要双清，之前辛苦配置的东西都无了

### SafetyNet
在刷好系统之后，我自然是想打开 ingress 玩下，然后折腾了半天，一直在提醒 ”ingress 需要安全登录“，一开始还以为是代理的问题，疯狂切换代理都没有用，后来查到[这个讨论](https://community.ingress.com/en/discussion/9303/ingress-requires-a-secure-login)发现是 SafetyNet 的问题，于是 Magisk 刷入了 [MagiskHide Props Config](https://github.com/cnrd/MagiskHide-Props-Config)、[Universal SafetyNet Fix](https://github.com/kdrag0n/safetynet-fix) 两个模块解决了这个问题

Universal SafetyNet Fix 这个模块无需任何配置，直接刷入即可生效
MagiskHide Props Config 这个则需要在shell执行指令 `props` 按照提示选择即可。
![](https://cdn.6-d.cc/img/20220501001.jpg)

### 相机
自带的相机 app 太拉了，直接停用，在 [Google Camera Port](https://www.celsoazevedo.com/files/android/google-camera/) 下载了个最新版本的相机，以及挑了个推荐的配置文件。

## 使用感受
原生的系统真是舒服啊，没有了一些有的没有的app，动画啥的感觉要比HOS要好。高帧率、AOD、蓝牙HD音频编码、屏下指纹这些都没有啥大问题。

甚至有些之前在HOS上面没有体验过的特性，比如说锁屏音乐可视化
![](https://cdn.6-d.cc/img/20220501002.jpg)

总的来说挺满意的，再看看后续使用的过程中有没有啥坑了，就这样。
