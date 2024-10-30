@echo off

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
call %cd%\miniconda3\condabin\conda.bat activate %cd%\miniconda3\envs\jupyterlab

@echo Activated environment: %CONDA_DEFAULT_ENV%

start python.exe open_dtale.py
