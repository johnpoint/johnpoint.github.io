---
title: 广东电信配置 IPTV-NET VLAN 单线复用
date:  2018-08-24 08:26:36
tags:
- IPTV
- VLAN
- 折腾
---

家里的弱电箱因为前期设计失误所以电视那里只有一条网线，而如果我想将 wifi 信号在屋子里面相对良好的覆盖的话我也要将无线路由器设置在电视机附近，但是 IPTV 也需要占用一条网线，一开始我们的解决方案是用一条劈叉的网线，但是数据传输会有质量问题，所以趁着暑假我就尝试着解决这个问题。

# 设置光猫

![](https://cdn.lvcshu.info/img/20200109001.png)

首先利用广东电信的光猫超级账户

```
SuperUser: telecomadmin
PassWord: nE7jA%5m
```

进行 VLAN 绑定

![](https://cdn.lvcshu.info/img/20200109002.png)

# 设置路由器

*注意：在进行这一个篇章的时候建议先对路由器的设置进行记录，以免~~机毁人亡~~*

## 交换机设置

![](https://cdn.lvcshu.info/img/20200109003.png)

```
光猫 --> WAN -------> LAN1(IPTV)
               |
               |----> CPU(NET)
```

![](https://cdn.lvcshu.info/img/20200109004.jpg)

然后就好了～

还可以顺便获取到 ipv6，双倍的快乐

