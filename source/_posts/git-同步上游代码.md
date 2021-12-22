---
title: git 同步上游代码
author: johnpoint
date: 2020-05-31 21:30:37
tags:
- 笔记
- git
---

```
git remote add upstream 上游地址
```
![](https://cdn.6-d.cc/img/20200531001.jpg)

```
git fetch upstream
git checkout master
git merge upstream/master
git merge upstream/master
git push origin master
```

> [Github:syncing a fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)