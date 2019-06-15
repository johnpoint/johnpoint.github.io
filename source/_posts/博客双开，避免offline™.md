---
title: 博客双开，避免offline™
author: johnpoint
date: 2018-08-07 05:30:37
tags:
- Github
- 折腾
- git
- blog
---

怎么双开博客呢？
答案就是—— vps 与 github 一起部署。。。
<!---more--->
好吧，我承认我是标题党了一下，主要是记录一下我 成功部署 完 hexo 博客了以后如何将博客部署到 github 上去。

# 创建远程仓库
就是在 github 上创建一个名称为 用户名.github.io 的仓库，这一个仓库可以在自动化部署之后在 用户名.github.io 生成博客，而用 github 在全世界（除中国大陆，中国大陆就是互联网上的孤岛）外厉害的 cdn ，我们的博客访问速度会比较快， 注意，一开始我是选择不初始化仓库，这样可以避免一些莫名奇妙的坑！

# 修改 站点配置
在 站点根目录 下的 `_config.yml` 寻找 `deploy` 关键词，将其 整部分 修改为：
```
deploy:
  type: git
  repo: GitHub上仓库的完整路径包括 .git
  branch: master
```
repo 的链接一定要是 ssh 而不是 https 的！！！

# 配置 git
生成 ssh 密钥
```
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的GitHub注册邮箱"
```
生成ssh密钥文件：
```
ssh-keygen -t rsa -C "你的GitHub注册邮箱"
```
然后直接三个回车即可，默认不需要设置密码
然后找到生成的 .ssh 的文件夹中的 `id_rsa.pub` 密钥，将内容全部复制

打开 GitHub_Settings_keys 页面，新建 `new SSH Key`

`Title` 为标题，任意填即可，将刚刚复制的 `id_rsa.pub` 内容粘贴进去，最后点击 `Add SSH key`。

大功告成！

>以上部分内容来自 [GitHub+Hexo 搭建个人网站详细教程](https://zhuanlan.zhihu.com/p/26625249)

推送博客至 github
好了，我们使用下面的一条指令就可以将博客推送到 github 上，实现某些意义上的 neveroffline™ 了！

撒花～～