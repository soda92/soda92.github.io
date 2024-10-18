---
layout: post
title:  "王者荣耀游戏分析"
date: 2024-10-18 9:30 +0800
categories: game dev life
---

## 方法

下载游戏安装包：[链接](https://pvp.qq.com)

使用“Android Studio" - Build - Analysis APK 分析

## 权限

读取安装应用
```xml
  <uses-permission
        android:name="android.permission.QUERY_ALL_PACKAGES" />
```

和三方应用互传消息
```xml
  <queries>

        <package
            android:name="com.tencent.mm" />

        <package
            android:name="com.unionpay" />

        <package
            android:name="com.vivo.game" />

        <package
            android:name="com.heytap.market" />

        <package
            android:name="com.tencent.mobileqq" />

        <package
            android:name="com.huawei.appmarket" />

        <package
            android:name="com.xiaomi.market" />

        <package
            android:name="com.ss.android.ugc.aweme" /> 抖音

        <package
            android:name="com.ss.android.ugc.aweme.lite" />

        <package
            android:name="com.ss.android.ugc.live" />

        <package
            android:name="com.tencent.weishi" />

        <package
            android:name="serviceconfig.wsds.cn.appserviceconfig" />

        <package
            android:name="com.tencent.cmocmna" /> 腾讯手游加速器

        <package
            android:name="com.tencent.xriver" />

        <package
            android:name="com.tencent.xfight" />

        <package
            android:name="com.tencent.gamehelper.smoba" />

        <package
            android:name="com.levelinfinite.sgameGlobal" />

        <package
            android:name="com.levelinfinite.sgameGlobal.midaspay" />

        <package
            android:name="com.levelinfinite.sgameGlobal.samsung" />

        <package
            android:name="com.levelinfinite.sgameGlobal.xiaomi" />

        <package
            android:name="com.levelinfinite.sgameGlobal.huawei" />

        <package
            android:name="com.smile.gifmaker" /> 快手

        <package
            android:name="com.kuaishou.nebula" /> 快手

        <package
            android:name="com.sina.weibo" />

        <package
            android:name="com.sina.weibog3" />

        <package
            android:name="com.tencent.qqlite" />

        <package
            android:name="com.duowan.kiwi" /> 虎牙

        <package
            android:name="air.tv.douyu.android" />

        <package
            android:name="tv.danmaku.bili" /> 哔哩哔哩

        <package
            android:name="com.tencent.qqlive" />

        <package
            android:name="com.cmcc.cmvideo" />

        <intent>

            <action
                android:name="com.huawei.hms.core.aidlservice" />
        </intent>

        <intent>

            <action
                android:name="com.huawei.hms.core" />
        </intent>

        <package
            android:name="com.xingin.xhs" /> 小红书
```


## 结论

这些平台通过`com.huawei.hms.core.aidlservice`相互共享消息。

只要装了任意一个应用，隐私就会可能泄露。

另外，这些应用占据了手机市场，形成了一个新的生活方式。可以称为“网络人 Internet-inspired people”。

普通的人就会被孤立。

所以以后要孤单的生活下去。


## 其他

加密

数据用了奇怪的ZSTD

![img]({{ site.url }}/assets/sgame-components.png)
![img]({{ site.url }}/assets/sgame-encrypted-data.png)

腾讯语音模型

![img]({{ site.url }}/assets/tencent-gamevoice-model.png)

成人、机器人验证

![img]({{ site.url }}/assets/sgame-adult-captcha.png)

一些设置

![img]({{ site.url }}/assets/sgame-dns-settings.png)

使用Python的错误检测

![img]({{ site.url }}/assets/sgame-error-xml.png)
![img]({{ site.url }}/assets/sgame-error-py.png)

使用了几个字体, 居然也用方正的

![img]({{ site.url }}/assets/sgame-fonts.png)
![img]({{ site.url }}/assets/sgame-fzyahei.png)

游戏内核用了Unity

![img]({{ site.url }}/assets/sgame-unity.png)

APP 图标

![img]({{ site.url }}/assets/sgame-icon.png)

## 其他的感觉

最近更新UI： ![img]({{ site.url }}/assets/sgame-new-match-ui.png)

擅长玩一个英雄后，匹配到的对手都是擅于玩那个英雄的。【游戏困难度增加】

信誉积分制导致必须打完玩一局。输了又想要赢回来。匹配没意思。【好胜心】

匹配界面右侧显示高手榜，都是段位比自己高的。让你想要排位上分，超过朋友。【攀比】
