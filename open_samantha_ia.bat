@echo off

title Samantha IA Server

@echo.
@echo.
@echo.
@echo ========================================
@echo     SAMANTHA IA - INTERFACE ASSISTANT
@echo ========================================
@echo.

:: For UTF-8 characters (shows latin accent letters)
chcp 65001
@echo.

@echo Current directory: %cd%
@echo.

@echo Activating 'samantha' virtual environment...

:: Activate 'base' virtual environment
call %cd%\miniconda3\condabin\conda.bat activate

:: Wait 3 seconds
TIMEOUT /t 3
@echo.

:: Activate 'samantha' virtual environment
call conda activate samantha

@echo Activated environment: %CONDA_DEFAULT_ENV%

::@echo.
::@echo.
::@echo.
::@echo ============================
::@echo     DOWNLOAD FIRST MODEL
::@echo ============================
::@echo.

:::: Check GGUF file on the current directory and download the first model
::dir *.gguf >nul 2>&1

::if %errorlevel% equ 0 (
::    echo GGUF model file found!
::    goto fim

::) else (

::    echo .GGUF file not found. Downloading capybarahermes-2.5-mistral-7b.Q4_K_M.gguf model...
::    @echo.
::    curl -L -O https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GGUF/resolve/main/capybarahermes-2.5-mistral-7b.Q4_K_M.gguf?download=true
    
::    echo .GGUF file not found. Downloading laser-dolphin-mixtral-2x7b-dpo.Q4_K_M.gguf model...
::    @echo.
::    curl -L -O https://huggingface.co/TheBloke/laser-dolphin-mixtral-2x7b-dpo-GGUF/resolve/main/laser-dolphin-mixtral-2x7b-dpo.Q4_K_M.gguf?download=true
    
::    echo Finished!
::)
:::fim

@echo.
@echo.
@echo.
@echo ===========================
@echo     STARTING SAMANTHA IA
@echo ===========================
@echo.

@echo Current directory: %cd%

@echo.
@echo Running 'python app.py' on terminal...

@echo.
@echo ===========================
@echo.

call python app.py

:: Press CTRL + SHIFT + ESC to open Windows Task Manager

::To show error messages before close terminal window
pause
exit
