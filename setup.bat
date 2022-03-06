@echo off
title DDoS-master Setup
echo #===========================[Setup]===========================#
echo 1. Download 'Python 3' (if not, or version is lower than '3.8')
echo.
pause
echo.
start https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe
echo 2. Install 'Python 3' (if not, or version is lower than '3.8')
echo.
pause
echo.
echo [i] Installing 'Python 3 Requirements'...
pip3 install -r requirements.txt
echo.
echo #===========================[Done!]===========================#
pause