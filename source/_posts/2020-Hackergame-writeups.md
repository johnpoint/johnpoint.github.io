---
title: Hackergame 2020 writeups
author: johnpoint
date: 2020-11-04 00:19:57
toc: true
tags:
- hackergame
- 记录
pressone: https://press.one/file/v?s=46a259eeb58a97ffa6878a64c1bd6113037d953e8519be3ab83f4f5e3307e2393ac04ab2dc1be975e61b44146290e80a2240ae2fc8935e403d64f17a1396ed6f00&h=5f3b0e15b699f1b56d2888ce858a76abeba2f009a891ac2c2d3fc1b9a32a9e20&a=79a3a060a7faa9dfc9b8b4e0a59bf3ebac305f78&hash_alg=sha256&v=3&f=P1
---

## 最终成绩

```
Sat Nov  7 09:59:22 AM CST 2020
当前分数：1500， 总排名：225 / 2415
binary：0 ， general：850 ， math：300 ， web：350
```
啊，我真的是太菜了（

只做出了一点点题目

## 签到

```
谢邀，利益相关：老签到出题人了。

今年出题组的要求是「来参加我们比赛的同学很多都是初学者，我们的签到题要清晰明确一点，让同学们轻松签到。」

我完全明白了，签到题就是送 flag，送就送，我最会送了.jpg

首先写好题目介绍：「你需要点击下面蓝色的 “打开/下载题目” 按钮，在打开的网页上获取到形如 flag{...} 的 flag，回到本页面，将其完整填写到下面的文本框中，并点击灰色的 “提交” 按钮即可完成本题。」

然后写一个 flag 提取器，选手要多少个 flag，我就给多少个 flag，绿色背景，红色加粗，显眼的位置，标准的格式，这都不叫送，那还有什么叫做送。

点击 「打开/下载题目」 按钮，打开 flag 提取器，获取第一个 flag 吧！

提示：完成题目遇到困难？你可以参考 2018 年签到题题解 与 2019 年签到题题解。
```

![](https://cdn.6-d.cc/img/20201104001.jpg)

F12 定位到拖动条，将最大值改为 1 然后将条拖到最大就可以得到 flag

```
<input type="range" id="number" name="number" class="form-control" value="0" min="0" max="1" step="0.00001">
```

## 猫咪问答++

```
在科大西区的研究生食堂旁边，有块水泥石板盛产肥猫。 每一个晴朗的中午，其上都会有花花白白的猫咪慵懒地晒着太阳。 而许多吃完午饭的同学，也可以趁此良机大肆撸猫。

但是突然从某一天起，水泥石板上多了一只猫首猫身的动物，拦住前来撸猫的同学，用它精心准备好的谜语考验他们。 只有全部答对了才可以撸猫，如果不小心答错了它就会炸毛给你看。

为了让每日撸猫活动恢复正轨，热心的 LUG 协会同学把这些谜题放到了这里。 如果你能答对所有的谜题，就会有 flag 作为奖励。

提示：正如撸猫不必亲自到现场，解出谜题也不需要是科大在校学生。解题遇到困难？你可以参考 2018 年猫咪问答题解。
```

![](https://cdn.6-d.cc/img/20201104003.jpg)

1. 手动数，数量为 **12**
2. 搜索到了 [wikipedia](https://zh.wikipedia.org/wiki/以鸟类为载体的网际协议) -> [RFC1149](https://tools.ietf.org/html/rfc1149)
>  A
   typical MTU is **256** milligrams.  Some datagram padding may be needed.

3. https://ftp.lug.ustc.edu.cn/活动/2019.09.21_SFD/slides/闪电演讲/Teeworlds/  --> Teeworlds 答案 **9**

4. 百度地图街景手动数 答案 **9**
5. https://news.ustclug.org/2019/12/hackergame-2019/ --> 答案 **17098**

## 2048

```
路漫漫其修远兮，FLXG 永不放弃！

要实现 FLXG，你需要过人的智慧，顽强的意志，和命运的眷属。只有在 2048 的世界里证明自己拥有这些宝贵的品质，实现「大成功」，你才有资格扛起 FLXG 的大旗。
```

![](https://cdn.6-d.cc/img/20201104004.jpg)

真就是 2048，看下 js 文件，发现里面有个 `game_manager.js`，粗略的浏览下逻辑，发现这么一句

```javascript
if (merged.value === 16384) self.won = true;
```

打断点，手动修改变量值，就成功了

![](https://cdn.6-d.cc/img/20201104005.jpg)

## 一闪而过的 Flag

```
深秋清晨，也西湖畔。一位可怜的同学蜷在路边的长椅上，用粗糙的手指敲击着残旧的神船笔记本，反复试图打开桌面上的一个程序。程序每次运行时隐约可见黑色控制台上有 flag 一闪而过。

在他的脚边搭着一块用废弃纸箱剪成的牌子，上面写着「我很可爱，请给我 flag」。路上的人行色匆匆，而那地上用来盛 flag 的饭盒依旧空空如也。

一位诗人同学路过，见此情景，遂把牌子改成了：「flag 来了，可是我什么也看不见！」

而你作为一名新生，不由动了恻隐之心。望着诗人潇洒远去的背影，你可以赶在下午诗人回来之前，帮助这位可怜的人，用 flag 装满他的饭盒吗?
```

啊这、啊这，我觉得这个 flag 是白给的啊，程序运行以后我瞬间截图就可以拿到 flag 了，之前还以为要录像逐帧判断...

## 从零开始的记账工具人

```
如同往常一样，你的 npy 突然丢给你一个购物账单：“我今天买了几个小玩意，你能帮我算一下一共花了多少钱吗？”

你心想：又双叒叕要开始吃土了 这不是很简单吗？电子表格里面一拖动就算出来了

只不过拿到账单之后你才注意到，似乎是为了剁手时更加的安心，这次的账单上面的金额全使用了中文大写数字

注意：请将账单总金额保留小数点后两位，放在 flag{} 中提交，例如总金额为 123.45 元时，你需要提交 flag{123.45}
```
[文件下载](https://cdn.6-d.cc/file/2020hackergame-bills.xlsx)

首先另存为 csv，使用 python 将 csv 转换为 json 下面比较好处理

统计源代码:

```python
import json


def cover(i):
    for j in range(0, len(text)):
        if text[j] == i:
            return j


yuan = 0
jiao = 0
fen = 0
text = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖", "拾"]

with open('bills.json', 'r') as f:
    a = json.load(f)
    for i in a:
        y = i["mon"].split("元")
        num = int(i["num"])
        for j in y:
            if "角" in j:
                jj = j.split("角")
                jiao += cover(jj[0])*num
                if len(jj) > 1 and "分" in jj[1]:
                    fen += cover(jj[1].split("分")[0])*num
                continue
            if "分" in j:
                fen += cover(j.split("分")[0].replace("零", ""))*num
                continue
            for i in range(0, len(j)):
                if j[i] == "整":
                    continue
                if j[i] == "佰":
                    continue
                if i+1 < len(j):
                    if j[i+1] == "拾":
                        yuan += cover(j[i])*10*num
                    elif j[i+1] == "佰":
                        yuan += cover(j[i])*100*num
                else:
                    if j[i] != "拾" and j[i] != "佰":
                        yuan += cover(j[i])*num
                if i-1 < 0 and j[i] == "拾":
                    yuan += 10*num

jiao += int(fen/10)
fen = fen % 10*0.01
yuan += int(jiao/10)
jiao = jiao % 10*0.1

print(yuan+jiao+fen)
print("y", yuan)
print("j", jiao)
print("f", fen)
```

答案 **20262.53**

## 来自一教的图片

```
小 P 在一教做傅里叶光学实验时，在实验室电脑的模拟程序里发现了这么一张的图片：
```

![](https://cdn.6-d.cc/img/20201104006.bmp)

```
数理基础并不扎实的小 P 并不知道什么东西成像会是这个样子：又或许什么东西都不是，毕竟这只是模拟 ... 但可以确定的是，这些看似奇怪的花纹里确实隐藏着一些信息，或许是地下金矿的藏宝图也未可知。
```

很简单，题目给足了提示，做一下傅立叶逆变换就可以得到

![](https://cdn.6-d.cc/img/20201104007.jpg)

## 超简单的世界模拟器

```
你知道生命游戏（Conway's Game of Life）吗？

你的任务是在生命游戏的世界中，复现出蝴蝶扇动翅膀，引起大洋彼岸风暴的效应。

通过改变左上角 15x15 的区域，在游戏演化 200 代之后，如果被特殊标注的正方形内的细胞被“清除”，你将会得到对应的 flag：

“清除”任意一个正方形，你将会得到第一个 flag。同时“清除”两个正方形，你将会得到第二个 flag。

注: 你的输入是 15 行文本，每行由 15 个 0 或者 1 组成，代表该区域的内容。
```
### 蝴蝶效应

我的解:
```
000000000000000
000000000000000
000000000000000
000000000000000
000000110000000
000001111000000
000001101100000
000000011000000
000000000000000
000000000000000
000000110000000
000001111000000
000001101100000
000000011000000
000000000000000
```
参考了 [知乎:生命游戏（Game of Life）有哪些图形？](https://www.zhihu.com/question/30782166)

## 233 同学的 Docker

```
233 同学在软工课上学到了 Docker 这种方便的东西，于是给自己的字符串工具项目写了一个 Dockerfile。

但是 233 同学突然发现它不小心把一个私密文件（flag.txt）打包进去了，于是写了一行命令删掉这个文件。

「既然已经删掉了，应该不会被人找出来吧？」233 想道。
```

Docker Hub 地址：[8b8d3c8324c7/stringtool](https://hub.docker.com/r/8b8d3c8324c7/stringtool)

从 Dockerfile 里面的命令来看

```
/bin/sh -c rm /code/flag.txt
```

flag 保存在了 `/code` 里面

看起来只需要提取 docker layers 里面的内容就好了，~~问题是我不会~~ 搜索到了 [Is there a way to tag a previous layer in a docker image or revert a commit?
](https://stackoverflow.com/questions/38234611/is-there-a-way-to-tag-a-previous-layer-in-a-docker-image-or-revert-a-commit)

```shell
docker save imagename $(sudo docker history -q imagename | tail -n +2 | grep -v \<missing\> | tr '\n' ' ') > image-caching.tar
```

使用这命令就把 layers 全部提取出来，接下来就每个 layers 都看看就好了

`flag{Docker_Layers!=PS_Layers_hhh}`

## 从零开始的火星文生活

```
一年一度的 Hackergame 就要到了，L 同学打算叫上 Q 同学一起去参加，却一连几天都见不到 Q 同学的人影。然而在比赛开始的前一天晚上却收到了来自 Q 同学的邮件：

Subject: 绝密！不要外传！！！
Body: 详情见附件
From: Q
L 同学打开附件一看，傻眼了，全都是意义不明的汉字。机智的 L 同学想到 Q 同学平时喜欢使用 GBK 编码，也许是打开方式不对。结果用 GBK 打开却看到了一堆夹杂着日语和数字的火星文……

L 同学彻底懵逼了，几经周折，TA 找到了科大最负盛名的火星文专家 (你)。依靠多年的字符编码解码的经验，你可以破译 Q 同学发来的火星文是什么意思吗？

注：正确的 flag 全部由 ASCII 字符组成！
```
文件内容：
```
脦脪鹿楼脝脝脕脣 拢脠拢谩拢茫拢毛拢氓拢貌拢莽拢谩拢铆拢氓 碌脛路镁脦帽脝梅拢卢脥碌碌陆脕脣脣眉脙脟碌脛 拢忙拢矛拢谩拢莽拢卢脧脰脭脷脦脪掳脩 拢忙拢矛拢谩拢莽 路垄赂酶脛茫拢潞 拢忙拢矛拢谩拢莽拢没拢脠拢麓拢枚拢鲁拢脽拢脝拢玫拢脦拢脽拢梅拢卤拢脭拢猫拢脽拢鲁拢卯拢茫拢掳拢盲拢卤拢卯拢莽拢脽拢麓拢脦拢盲拢脽拢盲拢鲁拢茫拢掳拢脛拢卤拢卯拢脟拢脽拢鹿拢帽拢脛拢虏拢脪拢赂拢猫拢贸拢媒 驴矛脠楼卤脠脠眉脝陆脤篓脤谩陆禄掳脡拢隆 虏禄脪陋脭脵掳脩脮芒路脻脨脜脧垄脳陋路垄赂酶脝盲脣没脠脣脕脣拢卢脪陋脢脟卤禄路垄脧脰戮脥脭茫赂芒脕脣拢隆
```

额。。。这题目，我搜索 `拢 utf8` 的时候正好搜到了 [代码中包含的中文全为乱码，编码问题求请教！](https://www.v2ex.com/t/421212) 然后看了下回答

```
alcarl   2018-01-09 01:25:21 +08:00 via Android   ❤️ 3
先把这段字保存成 gb2312 编码的文件，然后转换成 utf8 编码，保存，然后再转换成 8859-1 保存，然后当成 gbk 打开就好了，=͟͟͞͞(꒪ᗜ꒪ ‧̣̥̇) 字是下面这样的
类：包含对文件的操作（为了便于调试和观察，我把网页信息写入了文件中，所以有了这个文件操作类）

参考 http://blog.zeerd.com/ffmpeg-c2c3-bug/
```

然后按照这操作就....就出来了...

```
我攻破了 Ｈａｃｋｅｒｇａｍｅ 的服务器，偷到了它们的 ｆｌａｇ，现在我把 ｆｌａｇ 发给你：
ｆｌａｇ｛Ｈ４ｖ３＿ＦｕＮ＿ｗ１Ｔｈ＿３ｎｃ０ｄ１ｎｇ＿４Ｎｄ＿ｄ３ｃ０Ｄ１ｎＧ＿９ｑＤ２Ｒ８ｈｓ｝
快去比赛平台提交吧！
不要再把这份信息转发给其他人了，要是被发现就糟糕了！
```

## 从零开始的 HTTP 链接

```
众所周知，数组下标应当从 0 开始。

同样的，TCP 端口也应当从 0 开始。为了实践这一点，我们把一个网站架设在服务器的 0 号端口上。

你能成功连接到 0 号端口并拿到 flag 吗？

点击下面的打开题目按钮是无法打开网页的，因为普通的浏览器会认为这是无效地址。
```

地址: http://202.38.93.111:0/

从题目就可以看出来，应该自己构造 http 请求就可以得到 flag

我的解法：

网上找了个 C 实现的 http get ([来源](https://blog.csdn.net/weixin_37569048/article/details/91047343))


```C
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <time.h>
#include <errno.h>
#include <signal.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/time.h>
#include <netinet/in.h>
#include <arpa/inet.h>
 
#define IPSTR "202.38.93.111" //服务器IP地址;
#define PORT 0
#define BUFSIZE 1024
 
int main(int argc, char **argv)
{
        int sockfd, ret, i, h;
        struct sockaddr_in servaddr;
        char str1[4096], str2[4096], buf[BUFSIZE], *str;
        socklen_t len;
        fd_set   t_set1;
        struct timeval  tv;
         
         //创建套接字
        if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0 ) {
                printf("创建网络连接失败,本线程即将终止---socket error!\n");
                exit(0);
        };
 
        bzero(&servaddr, sizeof(servaddr));
        servaddr.sin_family = AF_INET;
        servaddr.sin_port = htons(PORT);
        if (inet_pton(AF_INET, IPSTR, &servaddr.sin_addr) <= 0 ){
                printf("创建网络连接失败,本线程即将终止--inet_pton error!\n");
                exit(0);
        };
 
        if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0){
                printf("连接到服务器失败,connect error!\n");
                exit(0);
        }
        printf("与远端建立了连接\n");
        memset(str2, 0, 4096);
        str=(char *)malloc(128);
        len = strlen(str2);
        sprintf(str, "%d", len);
 
        memset(str1, 0, 4096);
        strcat(str1, "GET / HTTP/1.1\n");
        strcat(str1, "Host: 202.38.93.111\n");
        strcat(str1, "\n\n");
 
        // strcat(str1, str2);
        strcat(str1, "\r\n\r\n");
        printf("%s\n",str1);
 
        ret = write(sockfd,str1,strlen(str1));
        if (ret < 0) {
                printf("发送失败！错误代码是%d，错误信息是'%s'\n",errno, strerror(errno));
                exit(0);
        }else{
                printf("消息发送成功，共发送了%d个字节！\n\n", ret);
        }
 
        FD_ZERO(&t_set1);
        FD_SET(sockfd, &t_set1);
 
        while(1){
                sleep(2);
                tv.tv_sec= 0;
                tv.tv_usec= 0;
                h= 0;
                // printf("--------------->1\n");
                h= select(sockfd +1, &t_set1, NULL, NULL, &tv);
                // printf("--------------->2\n");
 
                //if (h == 0) continue;
                if (h < 0) {
                        close(sockfd);
                        printf("在读取数据报文时SELECT检测到异常，该异常导致线程终止！\n");
                        return -1;
                };
 
                if (h > 0){
                        memset(buf, 0, 4096);
                        i= read(sockfd, buf, 4095);
                        if (i==0){
                                close(sockfd);
                                printf("读取数据报文时发现远端关闭，该线程终止！\n");
                                return -1;
                        }
 
                        printf("%s\n", buf);
						break;
                }
        }
        close(sockfd);
 
 
        return 0;
}
```

得到 `index.html` 文件获知关键信息

```html
<script>
      const term = new Terminal();
      const fitAddon = new FitAddon.FitAddon();
      term.loadAddon(fitAddon);
      term.open(document.getElementById("terminal"));
      fitAddon.fit();
      window.addEventListener('resize', function(event) {
        fitAddon.fit();
      });
      var firstmsg = true;
      const socket = new WebSocket(
         "ws://202.38.93.111:0/shell"
      );
      const attachAddon = new AttachAddon.AttachAddon(socket);
      term.loadAddon(attachAddon);
      socket.onclose = event => {
        term.write("\nConnection closed");
      };
      socket.onmessage = event => {
        if (firstmsg) {
          firstmsg = false;
          let token = new URLSearchParams(window.location.search).get("token");
          window.history.replaceState({}, null, '/');
          if (token) {
            localStorage.setItem('token', token);
          } else {
            token = localStorage.getItem('token');
          }
          if (token) socket.send(token + "\n");
        }
      };
      term.focus();
    </script>
```

然后又[整了个](https://github.com/core1011/websocket) C++ 的 websocket，连上他的服务器，发送 token，flag 到手

```
easywsclient: connecting: host=202.38.93.111 port=0 path=/shell
Connected to: ws://202.38.93.111:0/shell
>>> 2533:MEUCIQCz8PiKvLdy1K7+TZJTwqM581W17UdJRfk3Q6hxPtr6sQIgb+Cy14NALA4ETpFQfXyfDhIxz10fyy0+t7GDEhEpS3c=

>>> Please input your token: 
>>> flag{TCP_P0RT_0_1s_re5erved_BUT_w0rks_e7e56860a1}
```

## 不经意传输

### 解密消息

```
某同学在某不知名百科网站上看到一个神奇的密码学协议，叫做「不经意传输」（Oblivious transfer）。

于是他按照网站上描述的「1–2 oblivious transfer」自己实现了协议中一方的逻辑，你可以作为另一方与之进行交互。

完全按照百科网站上的算法来实现的协议应该不会有什么问题吧？

点击下载 源代码

除了网页终端，你也可以通过 nc 202.38.93.111 10031 来连接
```

[源代码](https://cdn.6-d.cc/file/2020hackergame-OT.py)

搜索一下题目里面的 1–2 oblivious transfer 查到了 [这个](https://en.wikipedia.org/wiki/Oblivious_transfer#1%E2%80%932_oblivious_transfer)

然后打开 python 照上面的步骤一步一步就可以拿到解密的消息

`flag{U_R_0n_Th3_ha1f_way_0f_succe55_w0rk_h4rder!_163a930598}`

## 超安全的代理服务器

### 找到 Secret

```
在 2039 年，爆发了一场史无前例的疫情。为了便于在各地的同学访问某知名大学「裤子大」的网站进行「每日健康打卡」，小 C 同学为大家提供了这样一个代理服务。曾经信息安全专业出身的小 C 决定把这个代理设计成最安全的代理。

提示：浏览器可能会提示该 TLS 证书无效，与本题解法无关，信任即可。

公告：题目帮助页面（https://146.56.228.227/help）右下角的「管理中心」链接有误，应该与首页相同，都是指向 http://127.0.0.1:8080/
```

地址 https://146.56.228.227/

首先进入页面看看～

```
Notice: 我们已经向您 推送（PUSH） 了最新的 Secret ，但是你可能无法直接看到它。
```

去 google 了一下，找到了 [How to Test HTTP/2 Push using Google Chrome](https://techexpert.tips/chrome/how-to-test-http2-push-using-google-chrome/) 按照里面的指引，安装了 [HTTP/2 and SPDY indicator](https://chrome.google.com/webstore/detail/http2-and-spdy-indicator/mpbpobfflnpcgagjijhmgnchggcjblin?hl=en) 扩展，打开以后看到了

```
The net-internals events viewer and related functionality has been removed. Please use chrome://net-export to save netlogs and the external netlog_viewer to view them.
```

导出了一下 log，然后在 netlog_viewer 里面寻找这一个 http/2 会话，然后很容易就可以看到

```
t=1410 [st=281729]  HTTP2_SESSION_SEND_RST_STREAM
                    --> description = "Duplicate pushed stream with url: https://146.56.228.227/e3b2a173-d763-409e-807c-584d13a10c92"
                    --> error_code = "7 (REFUSED_STREAM)"
                    --> stream_id = 6
```

访问上面出现的 url，获得 flag `flag{d0_n0t_push_me}`

## 参考链接

- [维基百科: 以鸟类为载体的网际协议](https://zh.wikipedia.org/wiki/以鸟类为载体的网际协议)
- [USTC LUG FTP](https://ftp.lug.ustc.edu.cn/活动/2019.09.21_SFD/slides/闪电演讲/Teeworlds/)
- [百度地图-街景](https://map.baidu.com/search/%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6%E8%A5%BF%E6%A0%A1%E5%8C%BA%E5%9B%BE%E4%B9%A6%E9%A6%86/@13053789.384286607,3720237.564861493,19z/maptype%3DB_EARTH_MAP#panoid=09010500121705221534309496D&panotype=street&heading=342.17&pitch=-16.29&l=19&tn=B_NORMAL_MAP&sc=0&newmap=1&shareurl=1&pid=09010500121705221534309496D)
- [USTC LUG NEWS](https://news.ustclug.org/2019/12/hackergame-2019/)
- [stackoverflow: How to convert CSV file to multiline JSON?](https://stackoverflow.com/questions/19697846/how-to-convert-csv-file-to-multiline-json)
- [知乎: 生命游戏（Game of Life）有哪些图形？](https://www.zhihu.com/question/30782166)
- [stackoverflow: Is there a way to tag a previous layer in a docker image or revert a commit?
](https://stackoverflow.com/questions/38234611/is-there-a-way-to-tag-a-previous-layer-in-a-docker-image-or-revert-a-commit)
- [v2ex: 代码中包含的中文全为乱码，编码问题求请教！](https://www.v2ex.com/t/421212)
- [CSDN: C语言实现HTTP的GET和POST请求-一路奔跑94](https://blog.csdn.net/weixin_37569048/article/details/91047343)
- [github: core1011/websocket](https://github.com/core1011/websocket)
- [wikipedia: Oblivious_transfer](https://en.wikipedia.org/wiki/Oblivious_transfer#1%E2%80%932_oblivious_transfer)
- [How to Test HTTP/2 Push using Google Chrome](https://techexpert.tips/chrome/how-to-test-http2-push-using-google-chrome/)