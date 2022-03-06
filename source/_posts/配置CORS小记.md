---
title: 配置CORS小记
date: 2019-10-07 21:44:00
toc: true
tags:
- hexo
- 折腾
- blog
- 字体
- nginx
pressone: https://press.one/file/v?s=b56535d9f85b2136fc4e85f8fa7366cd8a70d556562fcfc5fa8dd53a8e5ee57519c00d36461aa88e290111cc4dcad55f1869a5348f1283c1555db7c3d7ccd47d01&h=fb875cd81a5e33cb55088b3ccd82e84331db49f4e1e06f1b2481ba5320f33ac7&a=79a3a060a7faa9dfc9b8b4e0a59bf3ebac305f78&v=3&f=P1
---

最近在折腾博客的字体，最终选定了这几个字体作为网站的字体<!--more--> ~~莫名绕口~~

- [方正兰亭纤黑](http://www.foundertype.com/index.php/FontInfo/index/id/216.html)
- [方正粗金陵](http://www.foundertype.com/index.php/FontInfo/index/id/202)
- Times New Roman
- Times
- serif

问题来了，在方正网站上面获取字体的授权是非商业的授权。即使我都是非商业的用途，但是为了减少我的风险，我还是选择把字体和项目分开(怕死.jpg)。

emmmmm 我不把字体整进主题里面我怎么去使用字体咧？网上的 font CDN 也不大可能有方正的字体...

最后就把字体放上了一个资源服务器 cdn.lvcshu.workers.dev 我的图片之类的外链的东西都全部扔在上面，就把字体扔到了 https://cdn.lvcshu.workers.dev/font/ 上面，如果你打开 F12->network 然后刷新的话，应该能发现有两个后缀为 ttf 的资源是从 cdn.lvcshu.workers.dev 加载的。

## 配置 CORS

事情并没有那么简单，从别的域名引用是一种叫做跨域请求的请求 ~~莫名绕口×2~~ ，但是这种请求会撞上浏览器的一种叫做 [Same-origin policy(同源策略)](https://en.wikipedia.org/wiki/Same-origin_policy) 的安全策略，好消息是这个策略也有相应的绕过方法 [Cross-origin resource sharing(CORS 跨来源资源共享)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) 这种技术规范就可以通过添加标头来进行资源的跨域名调用。顺便他还可以对资源的调用范围作出限制，毕竟我可不想碰到方正的法务团队(~~逃~~)。

具体配置如下

```
location /font {
    set $cors_origin "";
    if ($http_origin ~* "^https://blog.lvcshu.com$") {
            set $cors_origin $http_origin;
    }
    if ($http_origin ~* "^https://johnpoint.github.io$") {
            set $cors_origin $http_origin;
    }
    if ($http_origin ~* "^https://lvcshu.netlify.com$") {
            set $cors_origin $http_origin;
    }
    if ($request_method = 'OPTIONS') {
    return 204;
    }
    add_header Access-Control-Allow-Origin $cors_origin always;
    add_header Access-Control-Allow-Headers "Content-Type, Authorization" always;
    add_header Access-Control-Allow-Methods "GET, POST, OPTIONS, PUT, PATCH, DELETE, HEAD" always;
    add_header Access-Control-Max-Age 86400 always;
}
```

## 修改 CSS

但是如果在主题的项目 CSS 里面写死我的 url 的话，因为上面有域名限制是不会生效的，可不能这样误导别人啊 QAQ，所以就把 CSS 的字体的声明在项目中删去了，要想正确加载字体只需要在 `all.css` 中加入这一句

```
@font-face{font-family:"FZJL";src:url('字体所在url')}
@font-face{font-family:"FZLT";src: url('字体所在url')}
```
即可生效

### 参考
- [nginx 处理跨域 (cors)](https://juejin.im/entry/5c249af1e51d45392c42e833)
- [nginx 指定多个域名跨域请求配置](https://my.oschina.net/yzChen/blog/1573828)
