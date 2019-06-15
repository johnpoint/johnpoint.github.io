---
title: 安装Arch笔记
date: 2019-05-07 22:53
toc: true
tags:
- Arch
- 学习笔记
- 折腾
---

> Arch Linux（或 Arch /ˈɑːrtʃ/)）是一款基于 x86-64 架构的 Linux发行版。
<!--more-->

> Arch Linux 采用滚动发行模式来获取系统更新和软件的最新版本。系统安装映像只简单地包含系统主要组件。

> Arch Linux 以社区 Wiki 的形式提供文档，称为 [ArchWiki](https://www.archlinux.org/)。该 Wiki 经常编有特定主题的最新信息，受到了 Linux 社区的广泛认可，内容也应用在 Arch Linux 以外的领域。

这三句话贯穿了我安装 Arch 全过程，就记录一下 ~~免得我忘了~~ 吧。

# 下载安装镜像

安装镜像很小，直接下载即可

[>>传送门<<](https://www.archlinux.org/download/)

# 安装环境

- VirtualBox Graphical User Interface Version 5.2.18_Ubuntu r123745
    - Memory: 4096 MB
    - CPU: 4
    - BIOS 启动
    - Storage: 35 GB
    - Network: NAT

# 安装

## 验证网络连接

```
ping archlinux.org
```

## 更新系统时间

```
timedatectl set-ntp true
```

### 设置分区

#### 硬盘分区
```
fdisk /dev/sda
```

```
输入 n 新建分区
然后一路回车默认
最后 w 改变写入硬盘
```
#### 格式化分区

```
mkfs.ext4 /dev/sda1
```

## 安装系统

### 准备

#### 挂载分区

```
mount /dev/sda1 /mnt
```

#### 设置软件源

在 Wiki 的 [镜像源](https://wiki.archlinux.org/index.php/Mirrors_(简体中文)#中国)页面挑选适合的镜像。

我选择阿里的源

编辑源列表
```
vim /etc/pacman.d/mirrorlist
```
添加
```
Server = http://mirrors.aliyun.com/archlinux/$repo/os/$arch
```
### 安装基础系统

```
pacstrap /mnt base base-devel
```

### 设置新安装的系统

```
genfstab -U /mnt >> /mnt/etc/fstab
```
切换到新系统
```
arch-chroot /mnt
```
#### 安装必要的软件

```
pacman -S vim nano
```

#### 设置时区
```
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc
```

#### 设置本地化文本编码

```
nano /etc/locale.gen
```
加入
```
zh_CN.UTF-8 UTF-8
```
执行
```
locale-gen
```
```
nano /etc/locale.conf
```
加入
```
LANG=en_US.UTF-8
```

#### 设置 hostname && HOST

编辑 `/etc/hostname`

```
nano /etc/hosts
```

```
127.0.0.1   localhost
::1         localhost
127.0.1.1   arch.localdomain  arch
```

#### 账户设置

##### 修改 root 密码

```
passwd
```

##### 添加账户

```
useradd -m johnpoint
passwd johnpoint
```

#### 设置开机引导

##### 安装 Grub
```
pacman -S grub
```

##### 部署 Grub

```
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```

至此，arch 就安装完成了，图形界面什么的 ~~咕咕咕~~ 下次再说


