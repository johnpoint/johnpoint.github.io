---
title: Github commit添加verified标识
date: 2019-02-09 19:07
toc: true
tags:
- Github
- verified
- 笔记
- 折腾
---

>这是一篇笔记

>内容：Github commit添加verified标识
<!--more-->
![效果图](https://cdn.6-d.cc/img/20190209002.jpg)

就是一直以来都 ~~懒得~~ 忙得没有将这个事情做好 ~~但是其实这个东西好像并没有什么用~~

# 用户端
## 生成 GPG 密钥对
```bash
gpg --gen-key
```

```bash
gpg --list-keys
```
列出 GPG 密钥对
![列出 GPG 密钥对](https://cdn.6-d.cc/img/20190209003.jpg)

## 导出 public 文件
```bash
gpg --armor --output public-key.txt --export E081E7D64************29B7080083
gpg --armor --output private-key.txt --export-secret-keys
```

## 配置本地 Git

```bash
git config --global user.signingkey E081E7D64************29B7080083
git config --global commit.gpgsign true
```

# Github 端
```bash
cat public-key.txt
```
将结果填入 [Personal settings->SSH and GPG keys](https://github.com/settings/keys)

保存

![效果](https://cdn.6-d.cc/img/20190209004.jpg)

-EOF-
