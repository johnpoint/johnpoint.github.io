---
title: 编译安装 python 3.9
date: 2020-10-09 11:02:14
toc: true
tags:
- python
---

## 环境

Ubuntu 20.04.1 LTS focal x86_64

## 下载 && 解压缩

```
wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tar.xz
```

*解压xz文件需要软件包 `xz-utils`*

```
tar -Jxvf Python-3.9.0.tar.xz
```

## 编译 && 安装

```
cd Python-3.9.0
./configure
make
make install
```

## 错误解决方法

### No module named zlib

```
编译步骤中使用
./configure --with-zlib
```

### pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.

安装软件包
```
libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk8.5 libgdm-dev libdb4o-cil-dev libpcap-dev
```