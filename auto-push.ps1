$ErrorActionPreference = "Stop"

Set-Location -LiteralPath $PSScriptRoot

$status = git status --porcelain
if (-not $status) {
  Write-Host "Pushlanacak yeni degisiklik yok."
  exit 0
}

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

git add .
git commit -m "site guncelleme $timestamp"
git push origin main

Write-Host "Degisiklikler GitHub'a gonderildi."
