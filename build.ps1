Write-Host "=== mdviewer build ==="

if (-not (pip show pyinstaller 2>$null)) { pip install pyinstaller }

pyinstaller viewer.spec --clean

Write-Host ""
Write-Host "Done: dist\mdviewer.exe"
Read-Host "Press Enter to continue"
