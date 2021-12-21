---
layout: post
title:  "编译Qt"
date: 2021-12-21 12:55 +0800
categories: dev
---

# 编译Qt

1. 通过 Qt Maintaince Tool 下载源码。
1. 设置编译器环境:

```powershell
Push-Location "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build"
cmd /c "vcvars64.bat & set" |
ForEach-Object {
if ($_ -match "=") {
    $v = $_.split("=", 2); set-item -force -path "ENV:\$($v[0])" -value "$($v[1])"
}
}
Pop-Location
Write-Host -ForegroundColor Green "Visual Studio 2022 Command Prompt variables set."
```

1. configure:

为了兼容Win7，要设置`no-feature-d3d12`.

```powershell
# static
..\configure.bat -prefix C:\Qt\5.12.12\msvc2022-static -release -confirm-license -opensource -nomake examples -nomake tests -nomake tools -static -static-runtime -opengl dynamic -angle -combined-angle-lib -no-feature-d3d12
# dynamic
..\configure.bat -prefix C:\Qt\5.12.12\msvc2022-dynamic\ -debug-and-release -confirm-license -opensource -nomake examples -nomake tests -nomake tools -shared -opengl dynamic -angle -combined-angle-lib -no-feature-d3d12
```

1. 编译 & 安装：
```
$Env:CL="/MP"
nmake
nmake install
```