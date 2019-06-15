---
title: 优化Bash控制台显示
date: 2019-05-28 21:14:30
toc: true
tags:
- Bash
- 美化
- Ubuntu
---

=。=<!--more-->

给我的 Ubuntu 控制台窗口做了一些优化 (?)

因为觉得原来默认的 Bash 太丑了

就像这样

![](https://cdn.lvcshu.info/img/20190528001.png)

然后现在改成了这样

![](https://cdn.lvcshu.info/img/20190528002.png)

# 方法

修改 `.bashrc`

```
export PS1="[ \[\033[1;32m\]\W\[\033[0m\]\]\[\033[1;32m\[\033[0m\] ] $ "
alias short='export PS1="[ \[\033[1;32m\]\W\[\033[0m\]\]\[\033[1;32m\[\033[0m\] ] $ "'
alias long='export PS1="[ \[\033[1;33m\]\u \[\033[1;32m\]\w\[\033[0m\] ] $ " '
```