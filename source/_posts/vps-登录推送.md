---
title: vps 登录推送.md
date: 2020-09-13 13:10:21
tags:
- vps
- 安全
---

国内的云服务器大多数都自带了 ssh 登录提示功能，这个功能我觉得不错，但是在很多并没有深度定制系统镜像的云服务器服务商那里就没有远程登录提醒功能了，于是写了一个小脚本来实现远程登录就将登录信息推送至 telegram 的功能

文件名 `00-ssh-login-alarm-telegram.sh` (其实也可以自己自定义)，将文件放在 `/etc/profile.d` 目录下。

```bash
#!/bin/bash

#填入 telegram bot 的 token
token=
#填自己telegram的id
id=

#vps ip
vpsip=$(curl -s ip.sb -4)
#登录时间
logintime=$(TZ=UTC-8 date '+%Y-%m-%d %H:%M:%S')
#远程登录的ip
loginip=$(who -u am i 2>/dev/null| awk '{print $NF}'|sed -e 's/[()]//g')
#ip归属asn组织名称
loginfrom=$(curl -s https://api.ip.sb/geoip/${loginip} | jq .asn_organization)
curl -s "https://api.telegram.org/bot${token}/sendMessage?chat_id=${id}" --data-binary "&text=NewLogin:%0AVPS: ${vpsip}%0ATime: ${logintime}%0ALogin from:%0A${loginip}%0A${loginfrom}" > /dev/null
```

因为用到了 `jq` 作为解析 json 的工具，所以需要在包管理器中自行安装。

使用效果：
```
NewLogin:
VPS: ***.***.***.***
Time: 2020-09-13 12:41:24
Login from:
***.***.***.***
"asn_organization"
```

*脚本使用的 api 来自 ip.sb*