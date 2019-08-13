---
title: 写了个 Hexo 主题 hexo-theme-XvA
author: johnpoint
date: 2019-08-13 11:50:00
tags:
- hexo
- 主题
- 折腾
---

之前博客用的主题是移植自 Typecho 的 [Maupassant](https://github.com/tufu9441/maupassant-hexo) 主题，简洁，也挺好看，就是有点略显单调<!--more-->，~~暑假也有点闲~~ 于是就有了自己写一个适合自己的主题的想法。

折腾了下就有了现在我用的这个主题 [XvA](https://github.com/johnpoint/hexo-theme-XvA) ~~名字瞎起的没啥含义~~

# 特性

- 自适应屏幕的大小
- disqus 支持，还加上了 lazyload
- gitalk 支持
- 夜间模式
- 回到最顶按钮
- 自动生成友链页面（这个当时折腾了我好久 QAQ）

# 以下内容就是 Github 的 README

# <div align="center"><img src="https://raw.githubusercontent.com/johnpoint/hexo-theme-XvA/master/logo.png"></img></div>
<p align="center"><img src="https://img.shields.io/badge/Version-1.2.4-green"> <img src="https://img.shields.io/github/license/johnpoint/hexo-theme-XvA"> <img src="https://img.shields.io/badge/hexo-3.7%2B-green"> <img src="https://travis-ci.org/johnpoint/hexo-theme-XvA.svg?branch=master"> <a href="https://codebeat.co/projects/github-com-johnpoint-hexo-theme-xva-master"><img alt="codebeat badge" src="https://codebeat.co/badges/4ff53f5f-f14a-4c02-b359-f70508088cef" /></a></p>

一个简~~约~~单的 HEXO 主题

# Contents 目录

- [Install 安装](#Install-安装)
- [Configuration 配置](#Configuration-配置)
- [Demo 演示](#Demo-演示)
- [TODO 待实现](#TODO-待实现)
- [Thanks 致谢](#Thanks-致谢)
- [LICENSE 许可协议](#LICENSE-许可协议)

# Install 安装

```bash
git clone https://github.com/johnpoint/hexo-theme-XvA themes/XvA
cd themes/XvA
cp _config.example.yml _config.yml
```

# Configuration 配置

```yml
# 导航栏
menu:
  Home: /
  Archives: /archives

post_copyright:
  enable: false
  author: 
  copyright_text: 本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">知识共享署名-相同方式共享 4.0 国际许可协议</a>进行许可。

loading: false
totop: true
fancybox: true
sitesince: #页脚版权信息，年份 Footer copyright information, filled in the year

# 侧边栏
# sidebar
widget:
  tag:
    enable: false
    count: 10
  friends: # 友情链接 Links
    enable: false

# Links
# 友情链接
friends:
  pagetitle:
  list:
    - title: # 标题
      img: # 头像 Avatar
      url: # 链接地址
      desc: # 简介 description
      sidebar: false # 显示在侧边栏 Displayed in the sidebar
      page: false # 在独立页面显示 Displayed on a separate page


# 评论 二选一
# pick one of two
comment:
  disqus:
    enable: false
    shortname: 
    lazyload: false
  gitalk: # See https://github.com/gitalk/gitalk#Install
    enable: false
    owner:
    repo:
    oauth:
      client_id:
      client_secret:
    admin:
#     - johnpoint

# 网站统计
analytics:
  google:
    enable: false
    id: #UA-xxxxxx-x
  busuanzi: # 不蒜子网站统计
    enable: false
    text:
      head: # 描述 示例:本站访客数 Example: view
      end:  # 描述 单位 示例:人次 Example: times
      # 效果: 本站访客数 233 人次
      # effect: view 233 times

tagscloud:
  color:
    enable: false
    start: # Start color. You can use hex (#b700ff), rgba (rgba(183, 0, 255, 1)), hsla (hsla(283, 100%, 50%, 1)) or color keywords. This option only works when color is true.
    end: # End color. You can use hex (#b700ff), rgba (rgba(183, 0, 255, 1)), hsla (hsla(283, 100%, 50%, 1)) or color keywords. This option only works when color is true.
  text:
    min: 20 # 最小字体大小 Minimal font size
    max: 40 # 最大字体大小 Maximum font size
    unit: px # 字体尺寸单位 Unit of font size
```

# Demo 演示

- [hexo-theme-xva.github.io/](https://hexo-theme-xva.github.io/)
- [johnpoint's blog](https://blog.lvcshu.com)

# TODO 待实现

- [x] 侧边栏友情链接
- [x] disqus
- [x] google analytics
- [x] 文章版权声明
- [x] highlight.js 代码高亮
- [x] 独立友链页面
- [x] 独立标签云
- [x] 添加不蒜子访客统计
- [x] disqus lazyload
- [x] 修复手机部分字体不兼容
- [x] 图片窗口内打开
- [x] 回到顶部
- [x] 加载进度条
- [x] 夜间模式
- [x] 代码高亮优化
- [x] 侧边目录优化
- [x] ~~Gitment~~ Gitalk 支持
- [ ] 添加动画效果
- [ ] 不蒜子阅读量统计
- [ ] 多语言支持
- [ ] 一言 支持

# Thanks 致谢

- [twbs/bootstrap](https://github.com/twbs/bootstrap)
- [jQuery](https://github.com/jquery)
- [HubSpot/pace](https://github.com/HubSpot/PACE)
- [hexojs/hexo](https://github.com/hexojs/hexo)
- [gitalk/gitalk](https://github.com/gitalk/gitalk)

# LICENSE 许可协议

[GNU General Public License v3.0](https://github.com/johnpoint/hexo-theme-XvA/blob/master/LICENSE)