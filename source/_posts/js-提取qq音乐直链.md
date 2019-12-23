---
title: js 提取 QQ 音乐直链
author: johnpoint
date: 2019-12-12 17:19:57
tags:
- QQ音乐
- JS
- 折腾
pressone: https://press.one/file/v?s=1128b721b4c7ea3d2748911ff238691c9e42f470c78d37e8c52d3293a228e5bb443708f287422344acf36a3b31fc9c44ce2c5f5c00b8f321be33a74a10948e3601&h=9d526189f1fdfc453e2a7ba05d19fc13ace1ed7cc7737297b3f1588b3b3c70ff&a=79a3a060a7faa9dfc9b8b4e0a59bf3ebac305f78&f=P1&v=3
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