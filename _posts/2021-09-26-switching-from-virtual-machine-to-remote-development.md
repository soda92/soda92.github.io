---
layout: post
title:  "从虚拟环境切换到远程开发"
date: 2021-09-26 01:29:00 +0800
categories: dev
---

由于各种各样的原因, 总会用到Linux. 比如, 在Windows中不想使用庞大的Visual Studio时, 使用Visual Studio Code开发C++代码, 这时使用的时MinGW环境, 但调试时, 容器的内容却显示不出来. 应该是gdb在Windows中的pretty-printer的问题.

而在Linux中, 调试时, 容器的内容可以正常显示. 但是使用Linux系统, 总会有各种不方便的地方. 如不能使用QQ, 微信等, 或者需要各种workaround. 又会担心界面不美观等等.

然后我试了下在Windows上的虚拟机. 使用VirtualBox或VMware, 下载镜像, 一步步安装. 但这又带来了各种问题, 有时候会存储空间不够, 需要另外添加空间, 与主机交互不方便, 消耗内存和CPU, 运行缓慢, 需要手动进行各种配置(网卡, 内存, 备份, 代理) 等.

Multipass和vagrant解决了以上的部分问题. 不再需要手动配置, 可以使用简单的命令行来管理. 但在主机上运行会消耗内存, 下载软件又消耗流量. 想到我有一个服务器, 那可以使用远程开发吗?

于是试了试VSCode的Remote-SSH功能. 真的是太方便了. 工作区, shell, 调试功能, 都非常方便. 而且还可以转发端口, 让体验和本地开发一样. 远程的build在电脑关闭后还可以继续运行. (当然需要tmux挂起来啦)

另外, 将代码放到GitHub中, 可以随时访问.
