---
layout: post
title: psql常用命令
---

| 命令                   | 作用                                                |
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
