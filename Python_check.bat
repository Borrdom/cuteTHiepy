@echo off

rem Check if Python is already installed on the Machine
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Python\PythonCore" >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed.
    exit /b
)

rem Check if Python is already installed on the User profile
reg query "HKEY_CURRENT_USER\Software\Python\PythonCore" >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed.
    exit /b
)

rem Download Python installer (change the URL if needed)
echo Downloading Python installer...
mkdir "$($env:USERPROFILE)\AppData\Local\cuteTHiepy"
cd "$($env:USERPROFILE)\AppData\Local\cuteTHiepy"
wget "https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe" -O "$($env:USERPROFILE)\AppData\Local\cuteTHiepy\python-3.9.13-amd64.exe"



rem Install Python silently
echo Installing Python...
rem TargetDir="$($env:USERPROFILE)\AppData\Local\cuteTHiepy"
start /wait python-3.9.13-amd64.exe /quiet PrependPath=1

rem Wait for the installation to complete (10 seconds in this example)
timeout /t 10 >nul

echo Python installation completed.

