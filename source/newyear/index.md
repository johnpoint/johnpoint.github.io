---
title: new year
author: johnpoint
date: 2019-12-31 00:00:00
layout: page
description: 跨年
donate: false
comment: false
---

<center>
            <h1 id="nowDiv"></h1>
        </center>
<script>
var newyear=new Date("2020/01/01 00:00:00");
function show() {
        var date =newyear - new Date();
        var now = "";
        var t=parseInt(date/1000);
        var hour = parseInt(parseInt(date/1000)/3600);
        date=date-hour*3600;
        if (hour < 10) { hour = "0" + hour };
        now = now + hour + ":";
        var min = parseInt(parseInt(date/1000)/60);
        date=date-min*60;
        if (min < 10) { min = "0" + min };
        now = now + min + ":";
        var sec = date;
        if (sec < 10) { sec = "0" + sec };
        now = now + sec;
        document.getElementById("nowDiv").innerHTML = now;
        setTimeout("show()", 1000);
    }
    show();
</script>