@echo off
title Setup - Knowledge Base
echo ============================================
echo  Установка зависимостей Knowledge Base
echo ============================================
echo.

echo [1/2] Python-зависимости (FastAPI, Gemini, uvicorn)...
cd /d "%~dp0ai"
pip install -r requirements.txt
if errorlevel 1 (
    echo ОШИБКА: не удалось установить Python-зависимости.
    echo Убедитесь что Python и pip установлены.
    pause
    exit /b 1
)

echo.
echo [2/2] Node.js-зависимости (VitePress)...
cd /d "%~dp0site"
npm install
if errorlevel 1 (
    echo ОШИБКА: не удалось установить Node.js-зависимости.
    echo Убедитесь что Node.js установлен.
    pause
    exit /b 1
)

echo.
echo ============================================
echo  Готово! Запустите start.bat
echo ============================================
pause
