@echo off
setlocal
title DAT - Digital Accessibility Toolkit Launcher

:: Configuración de colores (Naranja RS 06)
color 06

echo ============================================
echo      DIGITAL ACCESSIBILITY TOOLKIT (DAT)
echo      BY ROBERT SALINAS 
echo ============================================

:: 1. Verificar si existe el entorno virtual
if not exist ".venv" (
    echo [INFO] Primera instalacion detectada...
    echo [INFO] Creando entorno virtual Python...
    python -m venv .venv
    
    echo [INFO] Instalando dependencias desde requirements.txt...
    call .venv\Scripts\activate
    pip install -r requirements.txt
    
    echo [SUCCESS] Instalacion completada.
) else (
    echo [INFO] Entorno virtual encontrado.
    call .venv\Scripts\activate
)

:: 2. Iniciar la aplicación (GUI Nativa)
echo [INFO] Iniciando Digital Accessibility Toolkit (GUI)...
:: Iniciamos el script api.py que ahora gestiona tanto el servidor como la ventana
python -m src.backend.api

:: 3. Finalizar
echo [OK] DAT se ha cerrado.
pause
exit
