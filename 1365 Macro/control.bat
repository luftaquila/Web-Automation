@echo off
set uaccheck=0
:CheckUAC
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    goto UACAccess
) else ( goto Done )
:UACAccess
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\uac_get_admin.vbs"
set params = %*:"=""
echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\uac_get_admin.vbs"
"%temp%\uac_get_admin.vbs"
del "%temp%\uac_get_admin.vbs"
exit /b
:Done
echo [%TIME%] 관리자 권한 획득
echo.
echo [%TIME%] w32time 서비스 개시 시도
echo.
net start w32time
echo [%TIME%] 응답 서버 시간 동기화 시도
echo.
timeout /t 1 > nul
w32tm /config /manualpeerlist:211.234.237.12 /syncfromflags:manual /update
echo.
timeout /t 1 > nul
echo [%TIME%] 서버 시간 동기화 완료
echo.
timeout /t 1 > nul
set /p id=아이디 입력:
set /p pwd=비밀번호 입력:
set /p code=코드 입력:
set /p start_hour=개시 시간 시 입력:
set /p start_minute=개시 시간 분 입력:

setlocal
cd /d %~dp0
start macro.ahk
python control.py %id% %pwd% %date% %time% %code% %start_hour% %start_minute%
pause
