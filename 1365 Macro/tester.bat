@echo off
setlocal
cd /d %~dp0
cd Resources

tester.exe
if not "ERRORLEVEL%" == "0" goto ERROR
goto OK

:ERROR
python tester.py
goto OK

:OK
pause
