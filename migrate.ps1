$names = (Get-ChildItem .\_posts\).name | ForEach-Object { ($_ -split "\.")[0] }

[array]::Reverse($names)

foreach ($a in $names) {
    Write-Host $a
}

foreach ($a in $names) {
    pandoc _posts\$a.md --from markdown --to ipynb -o source\$a.ipynb
}

