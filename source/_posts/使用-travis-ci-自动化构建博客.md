---
title: 使用 travis-ci 自动化构建博客
date: 2019-06-15 14:09:31
toc: true
tags:
- travis-ci
- 建站
---

之前的 hexo 博客我都是在电脑上进行生成然后 push 上 github repo，现在感觉有些麻烦 ~~就是懒~~ 所以就想着能不能用 travis-ci 自动化构建博客。<!--more-->

# 准备

## 创建分支

我采用的方法是在 github 仓库上创建两个分支，`master` 和 `source`，分别存放生成的网站文件以及源文件。

## 编写 travis 配置文件

文件内容如下：

```
language: node_js
node_js: stable
branches:
  only:
  - source
cache:
  apt: true
  yarn: true
  directories:
    - node_modules
before_install:
- git config --global user.name "johnpoint"
- git config --global user.email "me@lvcshu.com"
- curl -o- -L https://yarnpkg.com/install.sh | bash
- export PATH=$HOME/.yarn/bin:$PATH
- npm install -g hexo-cli
install:
- yarn
script:
- npm install hexo-renderer-pug --save
- npm install hexo-renderer-sass --save
- npm install hexo-generator-feed --save
- hexo clean
- hexo generate
after_success:
- cd ./public
- git init
- git add --all .
- git commit -m "Travis CI Auto Builder"
- git push --quiet https://$REPO_TOKEN@github.com/johnpoint/johnpoint.github.io
  master
```

## 配置 github 密钥

因为之前我是打开了 github 的双因素认证，所以 push 不能使用原来的 github 用户名 + 密码的方式进行身份认证了。

![](https://cdn.lvcshu.info/img/20190615001.png)

在上图的地方加入 name 为 REPO_TOKEN，value 为 [Personal access tokens](https://github.com/settings/tokens) 


# 等待开始构建

一般来说要做的工作就已经完成了，只需要静静的等待 travis-ci 的构建完成，这篇文章就是通过自动构建生成的

![](https://cdn.lvcshu.info/img/20190615002.png)