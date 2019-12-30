---
title: 2 0 2 0
author: johnpoint
date: 2019-12-31 00:00:00
layout: page
description: Coming Soon
donate: false
comment: false
---

<center>
<p>距离 2020 年仅剩</p>
            <h1 id="nowDiv"></h1>
        </center>
<script>
var newyear=new Date("2020/01/01 00:00:00");
function show() {
        var date =newyear - new Date();
        var now = "";
        var t=parseInt(date/1000);
        var hour = parseInt(parseInt(date/1000)/3600);
        if (hour < 10) { hour = "0" + hour };
        now = now + hour + " 小时 ";
        var min = parseInt((parseInt(date/1000)-3600*hour)/60);
        if (min < 10) { min = "0" + min };
        now = now + min + " 分钟 ";
        var sec = parseInt(parseInt(date/1000)-3600*hour-min*60);
        if (sec < 10) { sec = "0" + sec };
        now = now + sec+" 秒 ";
        document.getElementById("nowDiv").innerHTML = now;
        setTimeout("show()", 1000);
    }
    show();
</script>