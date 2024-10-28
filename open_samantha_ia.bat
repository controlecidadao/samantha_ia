@echo off
title Samantha IA Server

@echo.
@echo ========================================
@echo     SAMANTHA IA - INTERFACE ASSISTANT
@echo ========================================
@echo.

:: Habilitar UTF-8 para caracteres especiais
chcp 65001
@echo.

@echo Current directory: %cd%
@echo.

@echo Activating 'samantha' virtual environment...

:: Ativar o ambiente base do Miniconda
call %cd%\miniconda3\condabin\conda.bat activate %cd%\miniconda3\envs\samantha


:: Verificar se houve erro ao ativar o Miniconda
if errorlevel 1 (
    echo.
    echo Error: Failed to activate Miniconda base environment. Exiting.
    pause
    exit /b 1
)

:: Aguardar 3 segundos
TIMEOUT /t 3
@echo.

:: Ativar o ambiente virtual 'samantha'
call %cd%\miniconda3\condabin\conda.bat activate %cd%\miniconda3\envs\samantha

:: Verificar se houve erro ao ativar o ambiente
if errorlevel 1 (
    echo.
    echo Error: Failed to activate 'samantha' environment. Exiting.
    pause
    exit /b 1
)

@echo Activated environment: %CONDA_DEFAULT_ENV%
@echo.

@echo ===========================
@echo     STARTING SAMANTHA IA
@echo ===========================
@echo.

@echo Running 'python app.py' on terminal...
@echo.

:: Executar o aplicativo principal
call python app.py

:: Verificar se o Python encontrou um erro ao rodar o script
if errorlevel 1 (
    echo.
    echo Error: Python application failed to run. Please check for issues.
    pause
    exit /b 1
)

:: Instruções finais
@echo Press CTRL + SHIFT + ESC to open Windows Task Manager
pause
exit
