@echo off

rem Check if Python is already installed
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Python\PythonCore" >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed.
    exit /b
)

rem Download Python installer (change the URL if needed)
echo Downloading Python installer...
curl -o python-installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe

rem Install Python silently
echo Installing Python...
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

rem Wait for the installation to complete (10 seconds in this example)
timeout /t 10 >nul

echo Python installation completed.
