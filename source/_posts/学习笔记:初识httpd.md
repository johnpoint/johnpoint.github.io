---
title: 学习笔记:初识httpd
author: johnpoint
date: 2018-11-02 09:49:57
tags:
- httpd
- 学习笔记
- 折腾
---

>提醒：这只是一篇学习笔记，不保证语句通顺，仅作记录。

<!---more--->

# 学习目标
## 安装 httpd、php、mysql
- 建立 **两个** 虚拟主机建立网站，并申请 **SSL** 使其能够通过 **https** 访问

## 学习过程
### 安装
```
yum install https://mirrors.ustc.edu.cn/epel/epel-release-latest-6.noarch.rpm https://mirrors.ustc.edu.cn/remi/enterprise/remi-release-6.rpm

yum -y install yum-utils
yum-config-manager --enable remi-php72

yum -y install httpd  mysql  mysql-server  mysql-connector-odbc  mysql-devel  libdbi-dbd-mysql  openssl  mod_ssl  httpd-manual  mod_ssl  mod_perl  mod_auth_mysql

yum -y install php  php-mcrypt  php-cli  php-gd  php-curl  php-mysql  php-zip  php-fileinfo  php-fpm  php-xml  php-mbstring  php-ldap  php-xmlrpc  php-devel
```
设置开机启动

chkconfig httpd on  
chkconfig mysqld on
建立虚拟主机文件夹
cd /home
mkdir www
修改httpd配置文件
cd /etc/httpd/conf
vi httpd.conf
加入

Include /home/www/vhost.conf
解析域名
略

新建虚拟主机
建立虚拟主机路径
cd /home/www
mkdir hk.lvcshu.info
新建虚拟主机配置
vi vhost.conf
写入

<VirtualHost *:80>
    DocumentRoot /home/www/hk.lvcshu.info
    ServerName hk.lvcshu.info
    RewriteEngine on
    RewriteCond %{SERVER_PORT} !^443
    RewriteRule ^(.*)?$ https://%{SERVER_NAME}/$1 [R=permanent,L]
</VirtualHost>

<Directory "/home/www/hk.lvcshu.info">
    Options Indexes FollowSymLinks
    AllowOverride all
    Order Deny,Allow
    Deny from none
    Allow from all
</Directory>
建立一个简陋的主页
略

申请证书
使用 acme.sh 的开源项目

curl  https://get.acme.sh | sh

cd .acme.sh
acme.sh  --issue  -d hk.lvcshu.info --webroot  /home/www/hk.lvcshu.info/
证书路径：/root/.acme.sh/hk.lvcshu.info

SSLCertificateFile        /root/.acme.sh/hk.lvcshu.info/hk.lvcshu.info.cer
SSLCertificateKeyFile     /root/.acme.sh/hk.lvcshu.info/hk.lvcshu.info.key
配置 https
<VirtualHost *:443>
DocumentRoot   /home/www/hk.lvcshu.info
ServerName     hk.lvcshu.info
SSLEngine      on
SSLCertificateFile        /root/.acme.sh/hk.lvcshu.info/hk.lvcshu.info.cer
SSLCertificateKeyFile     /root/.acme.sh/hk.lvcshu.info/hk.lvcshu.info.key
</VirtualHost>
return 0;

更新：

其实有一个更加好的虚拟主机的管理方法，那就是一个网站用一个配置文件来管理，在配置文件 httpd.conf 中直接引入 /home/www/vhost/* 即可

例如在 `/home/www/vhost` 中 `hk.lvcshu.info.dom` 即为 `hk.lvcshu.info` 的配置文件。
