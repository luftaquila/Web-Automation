@echo off
setlocal
cd /d %~dp0
cd Resources

control.exe
if not "ERRORLEVEL%" == "0" goto ERROR
goto OK

:ERROR
python control.py
goto OK

:OK
pause
