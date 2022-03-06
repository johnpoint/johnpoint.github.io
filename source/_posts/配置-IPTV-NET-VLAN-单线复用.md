---
title: 配置 IPTV-NET VLAN 单线复用
date:  2020-01-09 21:00:00
tags:
- IPTV
- VLAN
- 折腾
pressone: https://press.one/file/v?s=4fa38e405e4ed9b29a047ef1bd53ef87032093307636e33c20a712512825e8ee7362b9f60604563fcbeff75141ce09fc47763afbd582934a680fa5f17bbfb99d00&h=36d5889d09acc39ac98332e2661dc9c1d348ce585eb8f6cce9127d865c3052aa&a=79a3a060a7faa9dfc9b8b4e0a59bf3ebac305f78&f=P1&v=3
---

家里的弱电箱因为前期设计失误所以电视那里只有一条网线，而如果我想将 wifi 信号在屋子里面相对良好的覆盖的话我也要将无线路由器设置在电视机附近，但是 IPTV 也需要占用一条网线，一开始我们的解决方案是用一条劈叉的网线，但是数据传输会有质量问题，所以趁着暑假我就尝试着解决这个问题。

# 设置光猫

![](https://cdn.lvcshu.workers.dev/img/20200109001.jpg)

首先利用广东电信的光猫超级账户

```
SuperUser: telecomadmin
PassWord: nE7jA%5m
```

进行 VLAN 绑定

![](https://cdn.lvcshu.workers.dev/img/20200109002.jpg)

# 设置路由器

*注意：在进行这一个篇章的时候建议先对路由器的设置进行记录，以免~~机毁人亡~~*

## 交换机设置

![](https://cdn.lvcshu.workers.dev/img/20200109003.jpg)

```
光猫 --> WAN -------> LAN1(IPTV)
               |
               |----> CPU(NET)
```

然后就好了～

还可以顺便获取到 ipv6，双倍的快乐

