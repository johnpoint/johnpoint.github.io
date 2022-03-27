---
title: 博客迁移到cloudflare踩坑
author: johnpoint
date: 2022-03-25 13:11:29
tags:
- cloudflare
- saas
- 自动构建
- 折腾
toc: true
---

好久不见，新年开始一直忙着毕业设计和实习找新的工作，一直没有空去将一些折腾过的东西记录成为博客，最近在写毕业设计的间隙终于对博客进行了一波优化，顺便写篇博客记录一下。
 
在过去的部署中，博客一直是采用多节点部署并且通过dnspod的分地区解析做流量调度，将流量解析到尽量近的节点来尽量保证博客访问的速度。而多个节点之间的博客文件同步一开始用的是定时任务从github上面更新，后来改成了使用syncthing进行同步，这种方法看起来比较蠢，但是也持续的保证了我的博客在这两年期间的顺畅访问。

最近在翻sukka大佬的博客过程中，看到了 cloudflare worker 可以联合 kv 存储用来部署静态网站，于是乎我就先将自托管的图片提供服务(就是一个存了图片的http服务)，部署到了 cloudflare 上面，测试速度以及延迟也相当不错，所以就想彻底的把博客这一套东西完全迁移到 cloudflare 上面去。

这样就能保证我博客在我不主动折腾的情况下保证极高的可靠性以及相对不错的响应速度。

## 404页面异常

在 `worker-site/index.js` 文件中，有一段逻辑是控制在url无法获取到文件的时候返回 `/404.html`。但是一部署上去我就发现了不对劲，这个404页面直接源代码显示，并没有被浏览器渲染出来。

经过F12大法查看network的response知道返回的数据中缺少了个指定响应数据格式的header。

修复这个情况只需要在返回响应的时候加上相应的header即可，代码修改可以参考[我提的PR](https://github.com/cloudflare/worker-sites-template/pull/63)


## 参考链接

- [将 Hexo 部署到 Cloudflare Workers Site 上的趟坑记录](https://blog.skk.moe/post/deploy-blog-to-cf-workers-site/)
