@echo off
echo === mdviewer build ===

pip show pyinstaller >nul 2>&1 || pip install pyinstaller

pyinstaller viewer.spec --clean

echo.
echo Done: dist\mdviewer.exe
pause
