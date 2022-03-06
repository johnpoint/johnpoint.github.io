---
title: 树莓派 docker 搭建 pi-dashboard
date: 2018-10-21 05:40:21
tags:
- 树莓派
- docker
pressone: https://press.one/file/v?s=6a10521d5178f085674b2263476e9152576e05760974be0c7803f2c3a1d0150d1516a3dcb3cafdedc05936d3a2b982213c2a0c9f282853d16e4f2fa6cfc95eb801&h=cc79baea14ae9311d7f84eff94c219b40bd7dbb17ea4aab1691ea800399322fc&a=79a3a060a7faa9dfc9b8b4e0a59bf3ebac305f78&v=3&f=P1
---

前一阵子我入手了一（台？）（个？）树莓派，但是一直都没有时间研究该用来做什么.... 然后无意间看见了一个叫做pi-dashboard 的小玩意儿 上一张图看看
<!--more-->
![](https://cdn.lvcshu.workers.dev/img/upload/1812/a6430c02dba0e979.png)
就是这样，性能看起来就比较方便了

# 安装docker
这里参考的是[docker 中文文档](https://yeasy.gitbooks.io/docker_practice/install/raspberry-pi.html)的安装过程
诶，用官方脚本一步搞定嘞
```bash
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh --mirror Aliyun
```

很快的。。。

# 使用docker一步搞定 pi-dashboard

```bash
sudo docker run -d --name docker-pi-dashboard -e 'LISTEN=1024' --net=host ecat/docker-pi-dashboard
```
来自[一键部署pi dashboard](https://zhuanlan.zhihu.com/p/34923907)

好了，就这么水完了...
