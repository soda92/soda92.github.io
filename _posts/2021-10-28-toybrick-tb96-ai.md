---
layout: post
title:  "toybrick板子折腾笔记"
date: 2021-10-28 09:16:00 +0800
categories: dev
---

# toybrick板子折腾笔记

在公司拿到了一个测试用的板子，tb96-ai + rk3399pro.

```bash
[toybrick@toybrick]~% cat /proc/device-tree/compatible
rockchip,rk3399pro-toybrick-96ai-linuxrockchip,rk3399pro
```

系统是fedora28.

## 设置ssh
连入键盘和鼠标, 编辑`/etc/ssh/sshd_config`, 将

```sshd_config
#Port 22
```

取消注释, 然后
```bash
sudo systemctl enable sshd
```

## 设置不启动GUI

为了减少CPU占用嘛.

```sh
systemctl set-default multi-user.target
```

要恢复的话

```sh
systemctl set-default graphical.target
```


## 设置shell自动登录

系统在登录后才会连接wifi，不知道为啥。

设置shell自动登录：参考[stackchange](https://unix.stackexchange.com/questions/401759/automatically-login-on-debian-9-2-1-command-line)

编辑`/etc/systemd/logind.conf`, 将`#NAutoVTs=6`改为`NAutoVTs=2`.

然后运行

```bash
systemctl edit getty@tty1
```

, 输入

```systemd_unit_file
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin toybrick --noclear %I 38400 linux
```

启用`getty@tty1.service`:

```bash
systemctl enable getty@tty1.service
```

然后重启.

## mirror设置

配置文件在`/etc/yum.repos.d`. 文件参考[github](https://github.com/soda92/fedora-repo-config).
编辑`/etc/dnf/dnf.conf`, 在最后加入`fastestmirror=1`.

## 软件升级

升级系统： [fedora wiki](https://docs.fedoraproject.org/en-US/quick-docs/dnf-system-upgrade/)。
只支持跨两个版本，所以我升级到了fedora 30.  (不知道会不会break原本的驱动和库

当时存储还不够(16G存储), 我删掉了~/.cache, python package, qtcreator才升级完成.

首先刷新一下:
```sh
sudo dnf upgrade --refresh
```
然后重启.

安装dnf-plugin-system-upgrade:
```
sudo dnf install dnf-plugin-system-upgrade
```

下载升级软件包:
```
sudo dnf system-upgrade download --releasever=30 --allowerasing --skip-broken
```

升级前需要先将locale设置为en_US, 不然会出现终端方块的情况.
```
sudo localectl set-locale LANG=en_US.utf8
```

升级:
```
sudo dnf system-upgrade reboot
```

## 安装软件

```bash
sudo dnf makecache
sudo dnf install vim ncdu zsh tmux qtcreator -y
chsh -s $(which zsh)
```

qtcreator是之前卸载的.

## 设置防火墙

针对ftp服务（vsftpd）：

```sh
sudo firewall-cmd --add-port=21/tcp
sudo firewall-cmd --runtime-to-permanent
```

查看允许的端口

```sh
sudo firewall-cmd --list-ports
```

参考：[fedora文档](https://docs.fedoraproject.org/en-US/quick-docs/firewalld/)

## 其他

查看开机启动时的错误:

```
systemctl --state=failed
```

## 待解决

iwd无法使用

查看iwd启动程序:
```
systemctl cat iwd
```

是`/usr/libexec/iwd`.

运行时的错误:

```
[toybrick@toybrick]~% /usr/libexec/iwd
DES support not found
No CBC(DES3_EDE) support found, certain TLS connections might fail
No Diffie-Hellman support found, WPS will not be available
No keyring restrictions support found.
No asymmetric key support found.
TLS based WPA-Enterprise authentication methods will not function.
Kernel 4.20+ is required for this feature.
The following options are missing in the kernel:
        CONFIG_CRYPTO_USER_API_SKCIPHER
        CONFIG_ASYMMETRIC_KEY_TYPE
        CONFIG_KEY_DH_OPERATIONS
        CONFIG_CRYPTO_ECB
        CONFIG_KEYS
        CONFIG_CRYPTO_CBC
        CONFIG_CRYPTO_DES
        CONFIG_CRYPTO_DES
        CONFIG_ASYMMETRIC_PUBLIC_KEY_SUBTYPE
        CONFIG_PKCS7_MESSAGE_PARSER
        CONFIG_X509_CERTIFICATE_PARSER
        CONFIG_PKCS8_PRIVATE_KEY_PARSER
The following optimized implementations might be available:
        CONFIG_CRYPTO_DES3_EDE_X86_64
        CONFIG_CRYPTO_DES3_EDE_X86_64
```

好像没有办法升级内核.

## 板子资料

[rocketchips](https://t.rock-chips.com/wiki.php)
