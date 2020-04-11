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
<p>距离 2021 年仅剩</p>
</center>
<center>
<p><font size="10" id="hr"></font> 小时 <font size="10" id="min"></font> 分钟 <font size="10" id="sec"></font> 秒</p>
</center>
<script>
var newyear=new Date("2021/01/01 00:00:00");
function show() {
        var date =newyear - new Date();
        var now = "";
        var t=parseInt(date/1000);
        var hour = parseInt(date/1000/3600);
        if (hour < 10) { hour = "0" + hour };
        document.getElementById("hr").innerHTML = hour;
        var min = parseInt((date/1000-3600*hour)/60);
        if (min < 10) { min = "0" + min };
        document.getElementById("min").innerHTML = min;
        var sec = parseInt(date/1000-3600*hour-min*60);
        if (sec < 10) { sec = "0" + sec };
        document.getElementById("sec").innerHTML = sec;
        setTimeout("show()", 1000);
    }
    show();
</script>