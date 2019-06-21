---
title: 改进SSL证书相关策略
author: johnpoint
date: 2019-01-10 11:11
toc: true
tags:
- SSL检测
- 证书分发
- 折腾
- 建站
---

自从使用了 docker 作为基础环境以后，我想着写一个能够服务进行统一集中管理的面板，一方面不想使用市面上使用比较广泛面板 ~~因为我做到他们不行啊啊啊~~，一方面也算是一种练习吧<!--more-->

# 简述

抬头看下网站证书，yes！已经更换成泛域名证书啦~
简单的说下现在已经实现的 ~~满是bug的~~ 功能，证书分发，前文提过我是集中一个面板进行管理，面板中集成一个文件 `getcerfile.php` 可以直接访问（当然是有鉴权的啦，证书什么的不鉴权放公网会凉的），证书选用 Let’s 签发泛域名证书这样就不用考虑证书签发的时候解析到底解析到哪台服务器上去了 ~~不用造多轮子了，ye~~

# 证书检测

这一部分主要是受了  Axton 大佬的启发 详情看 [这篇文章](https://flyhigher.top/develop/755.html) ，加上本人比较弱，且目前暂时还不想用上数据库存数据，所以目前是用文件 + shell 进行证书检查工作 配合 php 输出为不那么难看的页面 并且嵌入在面板中。

效果图：

![](https://i.loli.net/2019/01/10/5c36bc4ecd015.png)

emmmmmmmmm上传时发现自建图床好像出了问题。。考虑自己写一个？ ~~先咕咕咕为敬~~

代码如下：
```
#!/bin/sh

cat urlfile.list | while read line
do
  touch "data/$line"
  touch "data/$line.ca"
  curl https://$line -v -s -o /dev/null 2>"data/$line.ca"
  datee=$(date +'%F %H:%M')
  echo "最后检查: " $datee > "data/$line"

  data=$(cat "data/$line.ca" | grep 'subject:')
  echo "证书域名: " ${data##* subject: } >> "data/$line"

  data=$(cat "data/$line.ca" | grep 'start date:')
  data=$(date -d "${data##* start date: }" +'%F %H:%M:%S')
  echo "签发日期: "${data} >> "data/$line"
  startdate=$data

  data=$(cat "data/$line.ca" | grep 'expire date: ')
  data=$(date -d "${data##* expire date: }" +'%F %H:%M:%S')
  echo "失效日期: " $data >> "data/$line"
  enddate=$data

  data=$(cat "data/$line.ca" | grep 'issuer: ')
  echo "签发机构: "${data##* issuer: } >> "data/$line"

  data=$(cat "data/$line.ca" | grep 'SSL certificate verify ok.')
  echo "证书状态: "${data##* } >> "data/$line"

  startdate=$(date -d "${startdate}" +%s)
  enddate=$(date -d "${enddate}" +%s)
  datee=$(date -d "${datee}" +%s)

  long=$(($enddate-$startdate))
  datee=$(($datee-$startdate))
  datee=$(($datee*100))
  hundred=100
  persent=$(($datee/$long))

  echo "<div class=\"mdui-progress\"><div class=\"mdui-progress-determinate\" style=\"width: ${persent}%;\"></div></div>" >> "data/$line"

  rm "data/$line.ca"
done
```
展示的代码如下：
```
<?php
include_once 'config.php';
if ($_COOKIE["user"] == md5($username.$userpasswd)) {
    echo '<div class="mdui-panel" mdui-panel>';
    function listDir($dir)
    {
        if (is_dir($dir)) {
            if ($dh = opendir($dir)) {
                while (($file = readdir($dh)) !== false) {
                    if ($file != "." && $file != "..") {
                        echo '<div class="mdui-panel-item">';
                        echo '<div class="mdui-panel-item-header">'.'<div class="mdui-panel-item-title">'.$file.'</div>'.'<i class="mdui-panel-item-arrow mdui-icon material-icons">keyboard_arrow_down</i>'.'</div>';
                        echo '<div class="mdui-panel-item-body">';
                        $myfile = fopen("$dir/$file", "r") or die("Unable to open file!");
                        while (!feof($myfile)) {
                            echo '<p>'.fgets($myfile) . '</p>';
                        }
                        echo '</div></div>';
                        fclose($myfile);
                    }
                }
                closedir($dh);
            }
        } else {
            echo $dir . '<br>';
        }
    }
    listDir("./data");
    echo '</div>';
} else {
    echo 'error';
}
?>
```

# 证书分发

emmmm上面也看的出来我是用 user 和 passwd md5一下写进cookie进行验证的，需要验证的 域名直接存放在 `urlfile.list` 文件里面 (我实在是太菜了)

同理分发证书也利用 cookie 进行身份验证

```
<?php
include_once 'config.php';
if ($_COOKIE["user"] == md5($username.$userpasswd)) {
    $myfile = fopen($_GET['file'], "r") or die("Unable to open file!");
    echo fread($myfile, filesize($_GET['file']));
    fclose($myfile);
} else {
    header("Location: /index.php");
}
?>
```
然后直接读取证书文件进行直接输出，同时 nginx 那儿对文件目录进行权限控制，获取证书使用

```
curl https://****/getcerfile.php?file=ssl/lvcshu.com/lvcshu.com.key -H 'cookie: user=？？？' > lvcshu.com.key
```

获取，这样在需要部署证书服务器上定时执行脚本可以更新证书了，同时 泛域名证书 使用 acme.sh 进行自动续期 emmmmmmmm 差不多这样如各位大佬发现什么不妥地方记得及时联系我啊 QAQ
Telegram:[@johnpoint](https://t.me/johnpoint)
