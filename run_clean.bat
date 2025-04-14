@echo off
cd /d %~dp0
set PATH=C:\Windows\System32

:: 執行打包好的 EXE
dist\run_server.exe

pause
