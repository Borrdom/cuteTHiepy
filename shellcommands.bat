mkdir "$($env:USERPROFILE)\AppData\Local\cuteTHiepy"
cd "$($env:USERPROFILE)\AppData\Local\cuteTHiepy"
wget "https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe" -O "$($env:USERPROFILE)\AppData\Local\cuteTHiepy\python-3.9.13-amd64.exe"
.\python-3.9.13-amd64.exe  /quiet TargetDir="$($env:USERPROFILE)\AppData\Local\cuteTHiepy" DefaultJustForMeTargetDir="$($env:USERPROFILE)\AppData\Local\cuteTHiepy"
wget "https://github.com/Borrdom/cuteTHiepy/raw/main/cuteTHiepy/plots.py" -O "plots.py"   
@REM cd %USERPROFILE%
@REM xcopy "W:\Aktuelle Listen\PC-SAFT_JourFix\cuteTHiepy\" %USERPROFILE%
wget "https://www.python.org/ftp/python/3.9.13/python-3.9.13.exe" -O "C:\GitHub_Projects\cuteTHiepy\python-3.9.13.exe" 

%USERPROFILE%\AppData\Local\Programs\Python\Python39\python -m pip install matplotlib


python -m pip install --upgrade pip
python -m pip install numpy  
python -m pip install numba 
.\tmp\python - 
.\python -m pip install matplotlib
.\tmp\python -m pip install pandas