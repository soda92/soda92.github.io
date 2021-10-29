---
layout: post
title:  "新电脑配置"
date: 2021-10-29 00:10:00 +0800
categories: dev
---

公司发了工作电脑，是笔记本ThinkBook 14 Gen2 ITL。有16GB运存和512G存储。由于我已经有了一个用来工作的笔记本，这个笔记本就被我拿到宿舍自己用了。小巧方便。

# 系统更新

联网激活系统后，首先下载更新。更新到了Windows 11.

# 安装软件

主要有V2ray、Chrome、Windows Terminal、VSCode、Telegram Desktop. 我还安装了VirtualBox用来运行虚拟机。

对了，还有Git for Windows。

## 虚拟机设置

安装系统后，添加网卡，设置固定IP，然后启用ssh。

通过ssh连接后，升级系统，安装常用软件。

安装[cockpit](https://cockpit-project.org/running.html#fedora)

```
sudo dnf install cockpit
sudo systemctl enable --now cockpit.socket
sudo firewall-cmd --add-service=cockpit
sudo firewall-cmd --add-service=cockpit --permanent
```

web控制台在9090端口。

## Windows Terminal设置

更改默认配色为One Half Dark，下载[Recursive Font](https://recursive.design), 更改字体为Rec Mono Linear.

设置默认字号为14，窗口大小为80*24，光标为实心框。

设置Ctrl+D退出([参考](https://stackoverflow.com/a/53577474/12291425))：
```
Set-PSReadlineKeyHandler -Key ctrl+d -Function ViExit
```

# 卸载软件

卸载联想电脑管家。
