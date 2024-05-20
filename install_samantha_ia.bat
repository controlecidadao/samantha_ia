@echo off


setlocal

:inicio
cls
echo.
echo Bem-vindo!
echo.
echo Deseja instalar Samantha IA?
echo.
echo 1. Sim
echo 2. Nao
echo.
set /p opcao="Digite sua opcao (1 ou 2): "

if "%opcao%"=="1" (
    goto continuar
) else if "%opcao%"=="2" (
    echo.
    echo Encerrando o programa...
    echo.
    pause
    exit
) else (
    echo.
    echo Opcao invalida!
    echo.
    pause
    goto inicio
)

:continuar
echo.
echo Continuando a execucao...
echo.
:: Coloque aqui o restante do seu código que deve ser executado
pause

:endlocal



@echo.
chcp 65001
@echo.

:: THIS SCRIPT DOWNLOAD AND INSTALL MINICONDA

@echo =====================
@echo OBTÉM DIRETÓRIO ATUAL
@echo =====================
@echo.

:: Obtém o diretório atual
@echo Obtendo diretorio atual...
@echo Diretorio atual: %cd%


:: Verifica se a pasta 'miniconda3' já existe
::if exist miniconda3 (
::   @echo.
::   echo A pasta 'miniconda3' ja existe. Saindo da rotina...

::   TIMEOUT /t 10
::   exit
::)



@echo.
@echo.
@echo =================
@echo INSTALA MINICONDA
@echo =================
@echo.

@echo Criando pasta %cd%\miniconda3...
mkdir miniconda3
@echo.

:: Faz o download do instalador do Miniconda
@echo Realizando download do Miniconda...
curl -L -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

TIMEOUT /t 10
@echo.

:: Instala Miniconda com a versão mais recente do Python. Alguns computadores não reconhecem '/', mas apenas '\'
@echo Instalando Miniconda na pasta miniconda3...
start /WAIT "" Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%cd%/miniconda3
start /WAIT "" Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%cd%\miniconda3

:: Aguarda 3 segundos após o download finalizar
TIMEOUT /t 3
@echo.

:: Remove o instalador
@echo Removendo arquivo de instalacao do Miniconda...
DEL Miniconda3-latest-Windows-x86_64.exe

@echo.
@echo Rotina 'instala_miniconda' finalizada!
@echo.









@echo off

@echo =====================
@echo OBTEM DIRETORIO ATUAL
@echo =====================
@echo.

:: Obtém o diretório atual
@echo Obtendo diretorio atual...
@echo Diretorio atual: %cd%



@echo.
@echo.
@echo ===============================
@echo CRIA AMBIENTE VIRTUAL samantha
@echo ===============================
@echo.

:: Cria o ambiente virtual 'samantha' com Python 3.10
@echo Criando ambiente virtual 'samantha'...
call %cd%\miniconda3\condabin\conda.bat create -y -n samantha python=3.10

:: Ativa o ambiente virtual samantha
@echo Ativando ambiente virtual 'samantha'...
call %cd%\miniconda3\condabin\conda.bat activate

TIMEOUT /t 3
@echo.

:: Ativa o ambiente virtual samantha
call conda activate samantha

@echo Ambiente ativado: %CONDA_DEFAULT_ENV%

@echo Exibindo lista de bibliotecas instaladas no ambiente %CONDA_DEFAULT_ENV%
call pip list
@echo.

:: Limpa módulos salvos no cache
::call pip cache purge

:: Instala as dependências do Ambiente Virtual 'samantha'.
call pip install -r requirements.txt

:: Instala Playwright
call playwright install

@echo Exibindo lista de bibliotecas instaladas no ambiente %CONDA_DEFAULT_ENV%
call pip list

@echo.
@echo Rotina 'Cria Ambiente Virtual samantha' finalizada!
@echo.

pause
exit
