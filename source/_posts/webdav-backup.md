---
title: 使用 Webdav 备份
author: johnpoint
date: 2020-11-07 10:19:57
tags:
- webdav
- 备份
- 折腾
---

## webdav

### 服务端

使用 [cloudreve](https://cloudreve.org/) 自带 webdav 

### 客户端

[cadaver](http://www.webdav.org/cadaver/)

## 备份

### 记录登录信息

`.netrc`
```
machine WEBDAVURL
login USERNAME
password PASSWORD
```

### 使用脚本

```bash
figlet webdav backup
echo "=========================================================================="
export t=`date +%Y-%m-%d`
echo "Backup: " $t
printf "集中配置文件 [执行中]"
mkdir config
cp .ssh/config config

......

printf "\r集中配置文件 [完成]              \n"
printf "归档配置文件 [执行中]"
zip -q backup.zip config -r
rm config -rf
printf "\r归档配置文件 [完成]              \n"

......

printf "\r归档密钥文件 [完成]              \n"
echo "put backup-"$t".zip" > webdav
echo "bye" >> webdav
cadaver WEBDAVURL < webdav
rm webdav
rm backup-$t.zip
echo "=========================================================================="
printf "备份完成"
```