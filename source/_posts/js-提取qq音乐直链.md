---
title: js 提取 QQ 音乐直链
author: johnpoint
date: 2019-12-12 17:19:57
tags:
- QQ音乐
- JS
- 折腾
---

```js
function getSong(name) {
    window.location.href = "https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=" + name;
    var muname = $('.js_song')[0].href.replace('https://y.qq.com/n/yqq/song/', 'C400').replace('.html', '');
    var qq = "0";
    var guid = "0";
    $.ajax({
        url: "https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=0&loginUin=" + qq +
            "&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&uin=" + qq + "&songmid=" +
            muname.replace('C400', '') + "&filename=" + muname + ".m4a&guid=" + guid,
        success: function (data) {
            data = JSON.parse(data);
            vkey = data.data.items[0].vkey;
            console.log($('.js_song')[0].href.replace('https://y.qq.com/n/yqq/song/', 'http://isure.stream.qqmusic.qq.com/C400').replace('.html', '.m4a?guid=' + guid + '&vkey=' + vkey + '&uin=' + qq + '&fromtag=66'))
            window.open($('.js_song')[0].href.replace('https://y.qq.com/n/yqq/song/', 'http://isure.stream.qqmusic.qq.com/C400').replace('.html', '.m4a?guid=' + guid + '&vkey=' + vkey + '&uin=' + qq + '&fromtag=66'))
        }
    })
}
```