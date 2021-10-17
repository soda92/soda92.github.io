---
layout: post
title: 一个项目的fix
date: 2021-04-28 10:00:00 +0800
categories: dev
---

最近研究知识图谱，看到了两篇知识图谱的文章[[1]](https://zhuanlan.zhihu.com/p/337115405)[[2]](https://zhuanlan.zhihu.com/p/360877984)，里面提到了一个[项目](https://github.com/chizhu/KGQA_HLM)，本人下载下来后，遇到了一些错误，在此把fix的过程分享一下。

## 先看README

第一步就是pyltp库安装不上，上网搜索得知，[LTP库](https://ltp.ai/docs/quickstart.html)已经支持python了，只需要`pip install ltp`即可。

然后安装[neo4j](https://neo4j.com/download-center/#community)，选择对应的平台下载，解压后运行`bin/neo4j console`。此时终端显示：

```shell
2021-04-28 12:48:56.162+0000 INFO  Starting...
2021-04-28 12:48:58.117+0000 INFO  ======== Neo4j 4.1.8 ========
2021-04-28 12:48:59.236+0000 INFO  Performing postInitialization step for component 'security-users' with version 2 and status CURRENT
2021-04-28 12:48:59.236+0000 INFO  Updating the initial password in component 'security-users'
2021-04-28 12:48:59.721+0000 INFO  Bolt enabled on localhost:7687.
2021-04-28 12:49:00.579+0000 INFO  Remote interface available at http://localhost:7474/
2021-04-28 12:49:00.580+0000 INFO  Started.
```

然后访问[http://localhost:7474/](http://localhost:7474/)，使用默认用户名`neo4j`密码`neo4j`登录，然后修改密码。填入`config.py`中。

然后执行`python .\neo_db\creat_graph.py`，出现`ImportError`，在IDE中发现这一行标灰没什么用

```python
from py2neo import Graph, Node, Relationship,NodeSelector
```

删掉这一行就可以运行了。

由于把依赖从`pyltp`改为了`ltp`，涉及到的代码均要修改。首先是`KGQA/ltp.py`，修改后的代码如下。

```python
# -*- coding: utf-8 -*-
from ltp import LTP


def cut_words(words):
    ltp = LTP()
    seg, hidden = ltp.seg([words])
    pos = ltp.pos(hidden)
    return seg, pos


def get_target_array(words):
    arr = []
    seg, pos = cut_words(words)
    for k in zip(seg[0], pos[0]):
        if k[1] in ('nh', 'n'):
            arr.append(k[0])
    return arr
```

其他均为一些小的修改，具体可以查看[Git Repo](https://github.com/soda92/KGQA-HLM)。
