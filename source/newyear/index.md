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
function show() {
        var date = new Date();
        var now = "";
        now = date.getFullYear() + "-";
        now = now + (date.getMonth() + 1) + "-";
        now = now + date.getDate() + " ";
        var hour = date.getHours();
        if (hour < 10) { hour = "0" + hour };
        now = now + hour + ":";
        var min = date.getMinutes();
        if (min < 10) { min = "0" + min };
        now = now + min + ":";
        var sec = date.getSeconds();
        if (sec < 10) { sec = "0" + sec };
        now = now + sec;
        document.getElementById("nowDiv").innerHTML = now;
        setTimeout("show()", 1000);
    }
    show();
</script>