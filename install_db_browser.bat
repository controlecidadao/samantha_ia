:: ==============================
:: DOWNLOAD AND UNPACK DB BROWSER
:: ==============================

:: For UTF-8 characters (shows latin accent letters)
chcp 65001
@echo.

set "URL=https://download.sqlitebrowser.org/DB.Browser.for.SQLite-3.12.2-win64.zip"
set "TMP_FILE=%TEMP%\db_browser.zip"
set "INSTALL_DIR=%cd%"

echo Baixando dB browser Portable...
curl -o "%TMP_FILE%" "%URL%"

echo Descompactando o arquivo...
powershell -command "Expand-Archive -Path '%TMP_FILE%' -DestinationPath '%INSTALL_DIR%'"

echo Instalação concluída.
pause