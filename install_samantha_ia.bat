@echo off
setlocal

:: Initialize
:inicio
cls
echo.
echo Welcome!
echo.
echo Do you want to install Samantha Interface Assistant?
echo.
echo 1. Yes
echo 2. No
echo.
set /p opcao="Select your option (1 or 2): "

:: Input Validation
if "%opcao%"=="1" (
    goto continuar
) else if "%opcao%"=="2" (
    echo.
    echo Closing the program...
    echo.
    pause
    exit
) else (
    echo.
    echo Invalid option! Please enter 1 or 2.
    echo.
    pause
    goto inicio
)

:: Installation Steps
:continuar
echo.
echo Wise decision! Continuing the installation...
echo.
pause

:: Enable UTF-8
@echo.
chcp 65001
@echo.

:: Section: Miniconda Installation
@echo =========================
@echo GETTING CURRENT DIRECTORY
@echo =========================
@echo.
@echo Getting current directory...
set CURRENT_DIR=%cd%
@echo Current directory: %CURRENT_DIR%

:: Check if Miniconda directory already exists
if exist "%CURRENT_DIR%\miniconda3" (
   echo.
   echo The folder 'miniconda3' already exists.
   echo Removing existing installation...
   rmdir /s /q "%CURRENT_DIR%\miniconda3"
   echo Old installation removed. Continuing with new installation...
)

@echo.
@echo ====================
@echo INSTALLING MINICONDA
@echo ====================
@echo.
@echo Creating folder for Miniconda...
mkdir miniconda3
@echo.

:: Download the Miniconda installer with integrity check
@echo Downloading Miniconda...
set MINICONDA_URL=https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
curl -L -O %MINICONDA_URL%
if not exist Miniconda3-latest-Windows-x86_64.exe (
    echo.
    echo Error: Download failed. Exiting.
    pause
    exit /b 1
)

@echo.
@echo Verifying file integrity...
certutil -hashfile Miniconda3-latest-Windows-x86_64.exe SHA256

@echo.
@echo Installing Miniconda in %CURRENT_DIR%\miniconda3...
start /WAIT "" Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%CURRENT_DIR%\miniconda3
if errorlevel 1 (
    echo.
    echo Installation failed. Exiting.
    pause
    exit /b 1
)

:: Clean up installer
@echo Removing installer file...
DEL Miniconda3-latest-Windows-x86_64.exe
@echo Miniconda installation completed successfully!
@echo.

:: Section: Accept Terms of Service
@echo ================================
@echo ACCEPTING CONDA TERMS OF SERVICE
@echo ================================
@echo.

@echo Accepting Conda Terms of Service for required channels...
call %CURRENT_DIR%\miniconda3\condabin\conda.bat tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
if errorlevel 1 (
    echo.
    echo Failed to accept Terms of Service for main channel. Continuing anyway...
)

call %CURRENT_DIR%\miniconda3\condabin\conda.bat tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
if errorlevel 1 (
    echo.
    echo Failed to accept Terms of Service for r channel. Continuing anyway...
)

call %CURRENT_DIR%\miniconda3\condabin\conda.bat tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2
if errorlevel 1 (
    echo.
    echo Failed to accept Terms of Service for msys2 channel. Continuing anyway...
)

@echo Terms of Service acceptance completed.
@echo.

:: Section: Environment Setup
@echo =======================================
@echo CREATING VIRTUAL ENVIRONMENT 'samantha'
@echo =======================================
@echo.

:: Create the 'samantha' environment with Python 3.10
@echo Creating virtual environment 'samantha'...
call %CURRENT_DIR%\miniconda3\condabin\conda.bat create -y --prefix %CURRENT_DIR%\miniconda3\envs\samantha python=3.10
if errorlevel 1 (
    echo.
    echo Failed to create 'samantha' environment. Exiting.
    pause
    exit /b 1
)

@echo Activating 'samantha' environment...
call %CURRENT_DIR%\miniconda3\condabin\conda.bat activate %CURRENT_DIR%\miniconda3\envs\samantha
if errorlevel 1 (
    echo.
    echo Failed to activate 'samantha' environment. Exiting.
    pause
    exit /b 1
)

:: Install Git in the virtual environment without creating shortcuts
@echo Installing Git in 'samantha' environment without shortcuts...
call %CURRENT_DIR%\miniconda3\condabin\conda.bat install -y git --no-shortcuts --no-update-deps -c conda-forge -p %CURRENT_DIR%\miniconda3\envs\samantha
if errorlevel 1 (
    echo.
    echo Failed to install Git. Exiting.
    pause
    exit /b 1
)

@echo Installing dependencies for 'samantha'...
call pip install -r requirements_samantha.txt
if errorlevel 1 (
    echo.
    echo Failed to install dependencies. Exiting.
    pause
    exit /b 1
)
@echo.

@echo =========================================
@echo CREATING VIRTUAL ENVIRONMENT 'jupyterlab'
@echo =========================================
@echo.

:: Create the 'jupyterlab' environment with Python 3.10
@echo Creating virtual environment 'jupyterlab'...
call %CURRENT_DIR%\miniconda3\condabin\conda.bat create -y --prefix %CURRENT_DIR%\miniconda3\envs\jupyterlab python=3.10
if errorlevel 1 (
    echo.
    echo Failed to create 'jupyterlab' environment. Exiting.
    pause
    exit /b 1
)

@echo Activating 'jupyterlab' environment...
call %CURRENT_DIR%\miniconda3\condabin\conda.bat activate %CURRENT_DIR%\miniconda3\envs\jupyterlab
if errorlevel 1 (
    echo.
    echo Failed to activate 'jupyterlab' environment. Exiting.
    pause
    exit /b 1
)

@echo Installing dependencies for 'jupyterlab'...
call pip install -r requirements_jupyterlab.txt
if errorlevel 1 (
    echo.
    echo Failed to install dependencies. Exiting.
    pause
    exit /b 1
)
@echo.

@echo Installing Chromium for Playwright...
call pip install pytest-playwright
if errorlevel 1 (
    echo.
    echo Failed to install Chromium for Playwright. Exiting.
    pause
    exit /b 1
)
@echo.

@echo All tasks completed successfully!
pause
exit