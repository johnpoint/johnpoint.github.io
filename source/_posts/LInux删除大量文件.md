---
title: Linux 删除大量文件
date: 2019-10-20 13:40
tags:
- Linux
- 折腾
---

最近去看了下我的自动重连脚本的 log 文件夹<!--more-->

![](https://cdn.lvcshu.info/img/20191020001.png)

文件太多， `rm` 命令会提示参数太多不能执行

于是写了个 python 脚本来删除文件

```
import os
for pathname,dirnames,filenames in os.walk('/root'):
     for filename in filenames:
         if 'net.log' in filename:
             file=os.path.join(pathname,filename)
             os.remove(file)
print("OK")
```