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

:::: Check if Miniconda directory already exists
::if exist "%CURRENT_DIR%\miniconda3" (
::   echo.
::   echo The folder 'miniconda3' already exists. Exiting installation routine...
::   pause
::   exit
::)

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
:: Add checksum verification here if the expected hash is known, for example:
:: set expected_hash=your_expected_hash_here
:: if not "%hash%"=="%expected_hash%" (
::     echo.
::     echo Hash verification failed. Exiting.
::     exit /b 1
:: )

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


::@echo Installing C++ compilers in the environment...
::call %CURRENT_DIR%\miniconda3\condabin\conda.bat install -y -c conda-forge compilers
::if errorlevel 1 (
::    echo.
::    echo Failed to install C++ compilers. Exiting.
::    pause
::    exit /b 1
::)

::@echo Installing additional Windows toolchain...
::call %CURRENT_DIR%\miniconda3\condabin\conda.bat install -y -c conda-forge m2w64-toolchain libpython
::if errorlevel 1 (
::    echo.
::    echo Failed to install Windows toolchain. Exiting.
::    pause
::    exit /b 1
::)

:: Install o Git no ambiente virtual sem criar atalhos no menu
@echo Installing Git in the 'samantha' environment...
set MENUINST=simple
call %CURRENT_DIR%\miniconda3\condabin\conda.bat install -y git
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

@echo All tasks completed successfully!
pause
exit
