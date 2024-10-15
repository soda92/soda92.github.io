---
layout: post
title: psql常用命令
date: 2020-11-15 10:00:00 +0800
categories: dev
---

| 命令 Command                  | 作用              Action                                  |
| ---------------------- | --------------------------------------------------- |
| `\h [NAME] `           | help on syntax of SQL commands, \* for all commands |
| `\d[S+] `              | list tables, views, and sequences                   |
| `\d[S+] NAME `         | describe table, view, sequence, or index            |
| ` \l[+] [PATTERN]`     | list databases                                      |
| `\echo [-n] [STRING] ` | write string to standard output (-n for no newline) |
| `\i FILE `             | execute commands from file                          |
| `\cd [DIR] `           | change the current working directory                |
| ` \c[onnect]`          | connect to new database                             |
| `\conninfo `           | display information about current connection        |
| `\q `                  | quit psql                                           |
