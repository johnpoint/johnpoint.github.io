---
title: 树莓派 docker 搭建 pi-dashboard
date: 2018-10-21 05:40:21
tags:
- 树莓派
- docker
---

前一阵子我入手了一（台？）（个？）树莓派，但是一直都没有时间研究该用来做什么.... 然后无意间看见了一个叫做pi-dashboard 的小玩意儿 上一张图看看
<!--more-->
![](https://cdn.lvcshu.info/img/upload/1812/a6430c02dba0e979.png)
就是这样，性能看起来就比较方便了

# 安装docker
这里参考的是[docker 中文文档](https://yeasy.gitbooks.io/docker_practice/install/raspberry-pi.html)的安装过程
诶，用官方脚本一步搞定嘞
```
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh --mirror Aliyun
```

很快的。。。

# 使用docker一步搞定 pi-dashboard

```
sudo docker run -d --name docker-pi-dashboard -e 'LISTEN=1024' --net=host ecat/docker-pi-dashboard
```
来自[一键部署pi dashboard](https://zhuanlan.zhihu.com/p/34923907)

好了，就这么水完了...