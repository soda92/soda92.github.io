---
layout: post
title: TDLib编译错误
---

今天编译TDLib，出现了以下错误：

```make
td/tdutils/td/utils/crypto.cpp:899:25: error: too few arguments to function ‘int EVP_MAC_init(EVP_MAC_CTX*, const unsigned char*, size_t, const OSSL_PARAM*)’
  899 |   res = EVP_MAC_init(ctx);
      |                         ^
In file included from /home/soda/td/tdutils/td/utils/crypto.cpp:28:
/usr/local/include/openssl/evp.h:1179:5: note: declared here
 1179 | int EVP_MAC_init(EVP_MAC_CTX *ctx, const unsigned char *key, size_t keylen,
      |     ^~~~~~~~~~~~
```

应该是我安装的OpenSSL版本太新导致的（编译安装）。

搜索得到`EVP_MAC_init`的[文档](https://www.openssl.org/docs/manmaster/man3/EVP_MAC_init.html)，里面提到：

```c
int EVP_MAC_init(EVP_MAC_CTX *ctx, const unsigned char *key, size_t keylen,
                  const OSSL_PARAM params[]);
```

If key is NULL, the key must be set via params either as part of this call or separately using EVP_MAC_CTX_set_params().

于是做如下修改：

```diff
diff --git a/tdutils/td/utils/crypto.cpp b/tdutils/td/utils/crypto.cpp
index 7b033ad0..a342b75c 100644
--- a/tdutils/td/utils/crypto.cpp
+++ b/tdutils/td/utils/crypto.cpp
@@ -896,7 +896,7 @@ static void hmac_impl(const char *digest, Slice key, Slice message, MutableSlice

   int res = EVP_MAC_CTX_set_params(ctx, params);
   LOG_IF(FATAL, res != 1);
-  res = EVP_MAC_init(ctx);
+  res = EVP_MAC_init(ctx, NULL, 0, params);
   LOG_IF(FATAL, res != 1);
   res = EVP_MAC_update(ctx, message.ubegin(), message.size());
   LOG_IF(FATAL, res != 1);
```

编译成功（也不知道对不对）。
