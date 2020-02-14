---
title: Tiny File Manager 使用
date: 2020-02-14 11:20:00
tags:
  - 体验
  - 折腾
---

最近我的 ikoula 杜甫频繁出现问题，再三考虑之下还是将杜甫退掉了，然后在 letbox 重新买了一个大盘鸡作为我的储存服务器+PT 盒子。

但是 PT 下载好了的文件我得拉回本地，所以我就想在服务器上建个私有云盘，但是试来试去都没有啥好用的，最后用到了 [Tiny File Manager](https://tinyfilemanager.github.io/)

安装的话也很简单，只需要你的服务器上有网页服务器和 php 环境即可，将 [tinyfilemanager.php](https://raw.githubusercontent.com/prasathmani/tinyfilemanager/master/tinyfilemanager.php) 和 [translation.json](https://raw.githubusercontent.com/prasathmani/tinyfilemanager/master/translation.json) 放到目录下就好了

为了安全起见，我还在 nginx 上设置了权限限制，让这个目录下面的文件只能通过这个 php 文件下载。

```
location / {
  deny all;
}
location /index.php {
allow all;
}
```