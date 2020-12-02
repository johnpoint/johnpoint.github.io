---
title: NodeMCU 制作桌面天气时钟
author: johnpoint
date: 2020-12-02 23:00:37
tags:
- ESP8266
- ST7796
- SGP30
- NodeMCU
- 折腾
toc: true
---

其实我眼馋青萍空气检测仪很久了，但是要700+的价格实在是下不了手，于是萌生了自己做一个类似的桌面摆件的想法，一方面是想尝试下制作包含硬件的小玩意，一方面确实是想整一个摆件放在桌面。<!--more-->

## 选型

### 芯片

在正式开始采购元件以及编码之前要先选定这个摆件将要采用的元件，因为是第一次真正意义上做这种加入了硬件的摆件，所以选择了对新手比较友好的 NodeMCU 上面有 ESP8266 芯片，这样的话就可以同时解决网络通信的问题，同时 NodeMCU 支持 Arduino 方式编程，这就很方便了，网上有各种各样的库可以给我调用。

### 屏幕

由于是桌面摆件肯定要有个界面展示出来，OLED 屏幕成本太高了不考虑，最终选定了 [ST7796](http://www.lcdwiki.com/zh/4.0inch_SPI_Module_ST7796) 这块带触摸的 4 英寸 TFT 屏幕，一方面是价格还可以接受，另一方面是触摸屏也可以方便后续可以满足我可能突然想做触摸交互功能的想法（也许会一直只是想做）。

### 传感器

PM2.5 什么的数据公开的 API 其实已经够了，其实青萍空气检测仪打动我的点是那个二氧化碳检测的功能，所以这个摆件的二氧化碳检测功能是肯定要安排上的，空气检测模块就在淘宝那里找了个 SGP30，这个模块可以检测 CO2和 TVOC，也够用了。

## 编码

其实写这篇文章的时候，这个摆件的主要功能已经写完了，目前有这些功能

- OTA 升级，不用插 USB 就可以刷新固件
- 保存配置文件开机进行自动配置
- WIFI 连接失败自身开启热点让用户进行配网
- WEB 界面修改配置
- WEB 界面管理密码验证
- NTP 校对时间
- 通过和风天气 API 获取天气数据
- 监测 CO2 和 TVOC
- 天气预警信息显示
- 白天黑夜天气图标切换

### 引用库

```
TFT_eSPI.h 
SPI.h
TFT屏幕驱动 
https://github.com/Bodmer/TFT_eSPI

Arduino_JSON.h 
JSON 解析 
https://github.com/arduino-libraries/Arduino_JSON

NTP.h
NTP对时
https://github.com/sstaub/NTP

Adafruit_SGP30.h
SGP30 驱动
https://github.com/adafruit/Adafruit_SGP30

ArduinoOTA.h
OTA 支持
https://github.com/jandrassy/ArduinoOTA

ESP8266WiFi.h>
ESP8266WiFiMulti.h
ESP8266HTTPClient.h
FS.h
LittleFS.h
WiFiClient.h
ESP8266WebServer.h
https://github.com/esp8266/Arduino
```

### 天气图标

天气图标由于我不想转换图片格式所以我选择自己用 TFT_eSPI 库里面的绘图函数自己重新绘制图标，但是由于太懒，所以目前只绘制了我这边有出现过的天气，然后我又想不能晚上也显示太阳吧，于是又绘制了一部分图标，加上了夜晚图标切换功能。

### API 代理

在调试 api 的过程中我发现和风天气 API 有些地方返回的数据太多了，有些数据用不上，然后数据量太多有可能会触发软件看门狗导致 Reset，所以用 python 的 flask 糊了个洗数据的服务端。

## 成品

欢迎给我 Star~ https://github.com/johnpoint/Weather-Card

### 本体

![](https://cdn.lvcshu.info/img/20201202002.jpg)
![](https://cdn.lvcshu.info/img/20201202003.jpg)

### WEB 管理界面

![](https://cdn.lvcshu.info/img/20201202005.jpg)
![](https://cdn.lvcshu.info/img/20201202004.jpg)

## 后续

后续打算想想怎么把屏幕的布局改一下，右下角似乎有一些空，然后有可能做个 3D 打印的外壳。

嗯，ESP8266 真香，玩硬件真的是好容易产生 ~~快感(??)~~ 成就感。