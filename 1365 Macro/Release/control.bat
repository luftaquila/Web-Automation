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
echo [%TIME%] ������ ���� ȹ��
echo.
echo [%TIME%] w32time ���� ���� �õ�
echo.
net start w32time
echo [%TIME%] ���� ���� �ð� ����ȭ �õ�
echo.
timeout /t 1 > nul
w32tm /config /manualpeerlist:27.101.215.199 /syncfromflags:manual /update
echo.
timeout /t 1 > nul
echo [%TIME%] ���� �ð� ����ȭ �Ϸ�
echo.
timeout /t 1 > nul

setlocal
cd /d %~dp0
control
pause
