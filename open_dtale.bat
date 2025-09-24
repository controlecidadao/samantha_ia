@echo off
@echo =================
@echo EXECUTANDO D-TALE
@echo =================
@echo.

:: For UTF-8 characters (shows latin accent letters)
chcp 65001
@echo.

:: Obtém o diretório atual
@set CURRENT_DIR=%cd%
@echo Diretorio atual: %CURRENT_DIR%

:: Verifica se o Python do ambiente virtual existe
@if not exist "%CURRENT_DIR%\miniconda3\envs\jupyterlab\python.exe" (
    @echo ERRO: Python do ambiente 'jupyterlab' nao encontrado.
    @pause
    @exit /b 1
)

@echo Executando 'python open_dtale.py' diretamente do ambiente virtual...
@echo.
@"%CURRENT_DIR%\miniconda3\envs\jupyterlab\python.exe" open_dtale.py
@pause
@exit /b

