---
title: Linux 进程信息格式化
author: johnpoint
date: 2021-02-02 21:20:00
tags:
- Linux
- 折腾
---

2021 年了，转头看了下自己的服务器面板，发现还是那个半成品的样子...于是在这三天改了下代码，加入了 v2 api 接口，这个接口主要使用 Websocket 进行通信，虽然说服务端的压力其实不是很大，但是使用轮询进行数据的更新不仅会看到一坨一坨的请求，对我的渣渣电脑来说也有些吃力了，不过这篇文章的内容不是这个，改天再开一篇文章记录一下。

进程查看其实是很早之前就想做进面板的功能之一，但是受限于并没有找到现成的 go 第三方或者官方库，所以就放了一放 ~~（结果放了差不多一年）~~，刚好这几天在改面板的代码，索性就顺手把它做了。

进程查看没有库可以调用，就只能通过调用系统命令来进行查看，一般来说我看进程会使用 `ps -aux`，但是对于面板来说，这里输出的数据有点太多以及有点太乱（太乱指的是输出的数据不是计算机友好型结构），然后看了下网上网友们五花八门的命令，左拼右凑之后，最后成品是用的 `ps axc -o pid,user,stat,pcpu,pmem,command --sort -pcpu --no-header | sed 's/\ \+/\ /g'` 最终得到的数据是没有表头、连续空格被替换成一个空格的数据，我感觉这就够了，其余的交给前端处理。

前端代码截取如下

```javascript
let ps = server.Ps.split('\n');
ps.forEach(item = >{
    if (item.split(" ").length > 3) {
        item = item.split(" ") if (item[0] === "") {
            item = item.slice(1, item.length)
        }
        let i = {
            PID: item[0],
            User: item[1],
            State: item[2],
            Pcpu: item[3],
            Pmem: item[4],
            Command: item.slice(5, item.length).toString().replaceAll(",", " "),
        }
        this.psData.push(i)
    }
})
```

最后效果还不错~