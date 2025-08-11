@echo off
title Samantha IA Server

@echo.
@echo ====================================
@echo     SAMANTHA INTERFACE ASSISTANT
@echo ====================================
@echo.

:: Habilitar UTF-8 para caracteres especiais
::chcp 65001
::@echo.

@set CURRENT_DIR=%cd%
@echo Current directory: %CURRENT_DIR%
@echo.

@echo Activating 'samantha' virtual environment...
@echo.
@"%CURRENT_DIR%\miniconda3\envs\samantha\python.exe" "%CURRENT_DIR%\app.py"
@pause
@exit /b