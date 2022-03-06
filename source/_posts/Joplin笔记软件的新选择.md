---
title: Joplin：笔记软件的新选择
author: johnpoint
date: 2020-02-22 14:29:57
tags:
  - Joplin
  - 体验
  - 折腾
---

前几天 Linux 中国发了一篇[文章](https://linux.cn/article-11896-1.html)，里面介绍了 Joplin 这一款开源的笔记本软件，对于一个平时有那么一点待办事项的我来说，产生了一点点想尝试的念头。然后就去安装并体验了一下，总的来说，体验不错，但是仍然有着一点瑕疵。

# 使用体验

![](https://cdn.lvcshu.workers.dev/img/20200216001.jpg)
![](https://cdn.lvcshu.workers.dev/img/20200216002.jpg)
![](https://cdn.lvcshu.workers.dev/img/20200216003.jpg)

## 优点

- 支持 markdown、html
- 待办事项可以定时提醒
- 网页摘抄可以直接截取网页的 HTML 代码保存
- 中文本地化并不完全

## 一些坑

- onedriver 速度慢
- Dropbox Linux 版本无法授权
- 坚果云 webdav 有频率限制
- 自建 webdav 有点麻烦以及不能保证速度
- linux 桌面版本有时会无端卡顿
- 加密密钥不能编辑管理

# 安装

桌面端，我使用的是 Linux 系统，直接下载官网的 AppImage 文件，开箱即用。移动端直接从 GooglePlay 下载安装即可。

## 配置同步

一开始我使用的同步策略是使用自建 webdav 进行同步，但是效果不佳，后来我就去尝试使用了国内的坚果云 webdav 进行同步笔记，但是由于坚果云的 webdav 有频繁操作的保护，所以几乎是不可用的状态。

无奈之下我只能粗暴的选择直接进行文件同步，首先使用的 resilio sync 未知原因的同步速度十分缓慢(内网)，所以最后选择了同类型的软件 synthing

## 加密配置

Joplin 还自带加密的功能，但是加密的功能稍微有点设计缺陷，主要是操作了逻辑的缺陷，他没有设计加密密钥的删除功能，所以加密如果禁用再重新打开是不能用回之前的密钥的，只能重新生成，而且如果两个设备都生成了密钥两边都会有两把密钥，有点看不顺眼。

正确的操作逻辑：

```
启用加密-->同步-->输入密码
```

# 参考链接

- [Joplin：真正的 Evernote 开源替代品](https://linux.cn/article-11896-1.html)
- [Syncthing – 数据同步利器---自己的网盘，详细安装配置指南，内网使用，发现服务器配置](https://www.cnblogs.com/jackadam/p/8568833.html)
- [Joplin 同步到坚果云 webdav](https://zsxwz.com/2019/07/11/joplin%E5%90%8C%E6%AD%A5%E5%88%B0%E5%9D%9A%E6%9E%9C%E4%BA%91webdav/)
- [Syncthing 官网](https://syncthing.net/)

> PS:本篇文章在 Joplin 上完成
