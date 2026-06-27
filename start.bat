@echo off
title Knowledge Base

if not exist "%~dp0site\node_modules" (
    echo node_modules не найден, запускаю установку...
    call "%~dp0setup.bat"
)

cd /d "%~dp0ai"
start "FastAPI" cmd /k "python -m uvicorn server:app --reload"

cd /d "%~dp0site"
start "VitePress" cmd /k "npm run docs:dev:host"

timeout /t 8 /nobreak >nul
start "" "http://localhost:5173/infosec-knowledge-base-ai/"
