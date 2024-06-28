@echo off

::title D-Tale

@echo.
@echo =======================
@echo     STARTING D-TALE
@echo =======================
@echo.

:: For UTF-8 characters (shows latin accent letters)
chcp 65001
@echo.

@echo Current directory: %cd%
@echo.

@echo Activating 'jupyterlab' virtual environment...

:: Activate 'base' virtual environment
call %cd%\miniconda3\condabin\conda.bat activate

:: Wait 3 seconds
TIMEOUT /t 3
@echo.

:: Activate 'jupyterlab' virtual environment
call conda activate jupyterlab

@echo Activated environment: %CONDA_DEFAULT_ENV%

start python.exe open_dtale.py
::start "" pythonw.exe -m idlelib -e "open_dtale.py"
