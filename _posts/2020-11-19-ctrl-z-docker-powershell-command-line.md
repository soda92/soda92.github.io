---
layout: post
title: ctrl+z导致powershell中docker命令行意外退出
date: 2020-11-19 10:00:00 +0800
categories: dev
---

最近经常使用 pwsh（PowerShell Core）连接 docker 访问 PostgreSQL 数据库，当我编辑命令的时候，可以使用 Ctrl+左右方向键进行左右词间的跳转，或者使用 alt+backspace 进行以词为单位的删除。

I frequently use pwsh to access docker-based postgresql database recently. It supports Ctrl+left/right edit on the command line. Use alt+backspace can delete words.

然而，当我多删了一个词的时候，长时间使用文本编辑器的习惯使我按下了 ctrl+z，希望进行恢复。这时，意外发生了：docker 命令行退出，返回到了 pwsh prompt。

But, When I acceidently press more backspace, I want to use "ctrl+z" to recover. An incident happens: docker command exited!

我尝试进行了一些搜索：

I tried some searches:

- ctrl+z terminate docker terminal
- suspend and recover in powershell
- docker windows "ctrl z"

得到了一些相关的内容：

These are related contents:

- [alankent.me](https://alankent.me/2017/07/04/windows-powershell-control-z-and-kitemati/)
- [memotut.com](<https://memotut.com/solution-of-the-problem-that-ctrl+z-cannot-be-used-in-powershell-in-docker-for-windows-environment-(tentative)-3d0ce/>)

看起来，ctrl+z 会生成 EOF，这或许是导致问题的原因。相关的 blog post 中提到，在 powershell 中可以使用 Legacy mode（使用旧版控制台）来解决。然而，我使用的是 Windows Terminal，没有相关的选项。

It seems that Ctrl+z emits EOF, which might causes the problem. ALso in these posts the authors mentioned that we can use `legacy mode` to solve for CMD. But Since I use Windows Terminal, there is no such option.

最终，我想到了一种替代的方法：[自定义快捷键](https://docs.microsoft.com/en-us/windows/terminal/customize-settings/actions)。

At last I come up with an alternative method: [customize shortcuts](https://docs.microsoft.com/en-us/windows/terminal/customize-settings/actions)

我在 windows Terminal 的 settings.json 中放置了如下代码：

I put the following codes in Windows Terminal's settings.json:

```json
{
  "command": "commandPalette",
  "keys": "ctrl+z"
}
```

当然，也可以使用其他的command；这并不重要。这时，ctrl+z便会执行自定义的动作，而不是产生EOF。这或许会带来一些其他的影响；然而，这确实解决了我的问题。

Of course we can use other commands, this is not important. By doing this `Ctrl+Z` will perform custom action instead of emitting EOF.

This may have other effects but it really solves my problem.
