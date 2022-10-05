---
title: 使用 ssh 密钥签名 git commit
author: johnpoint
date: 2022-10-05 21:30:37
tags:
- git
---

在 [Github commit添加verified标识](https://blog.lvcshu.com/2019/02/09/Github-commit添加verified标识/) 这篇文章中，配置好了 gpg 密钥签名作为标识 git commit 是否值得信任带凭证，但是载后面使用签名的过程中渐渐感到了一丝丝的麻烦，因为 gpg 密钥在我日常的生活中并没有很多其他的用处。最近 [github 支持了显示通过 ssh 密钥签名的 commit 的功能](https://github.blog/changelog/2022-08-23-ssh-commit-verification-now-supported/)。ssh 密钥在日常用起来要比 gpg 密钥要多得多，所以配置了一下，顺便写个文章记录操作流程。

```shell
git config --global gpg.format ssh
git config --global user.signingKey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
git config --global tag.gpgsign true
```

一般来说，配置好了这几个选项，就可以顺利的把签名加上了，要是 git commit 的时候提示你 `ssh是不支持的格式` 那么就意味着当前版本的 git 并不支持通过 ssh 密钥签名 commit，这时候就要自己更新下系统上面的 git 了。