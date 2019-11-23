---
title: 修复Chrome色差问题
date: 2019-06-04 15:54:20
toc: true
tags:
- Chrome
- 色差
---

在几次使用 Chrome 发现了网页的色彩渲染似乎有些问题<!--more-->

如图

![左:telegram 预览图 右:Chrome 渲染图](https://cdn.lvcshu.info/img/20190604001.png)

可以很明显的发现色彩不一致，一开始我还以为是我的显示器的问题，直到发现了上面那一张图。

然后经过简单的搜索我也得到了[修复的方法](https://segmentfault.com/a/1190000012818983)

打开 [chrome://flags/#force-color-profile](chrome://flags/#force-color-profile)，将色彩配置设置为sRGB

![](https://cdn.lvcshu.info/img/20190604003.jpeg)

调整好以后效果就是这样的啦~

![左:telegram 预览图 右:Chrome 渲染图](https://cdn.lvcshu.info/img/20190604002.png)

