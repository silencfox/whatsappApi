#!/bin/bash

# Iniciar Xvfb en segundo plano
Xvfb :99 -screen 0 1024x768x16 &

# Exportar la pantalla para que pywhatkit use Xvfb
export DISPLAY=:99

# Iniciar Chromium con la carpeta de persistencia de sesión
chromium --user-data-dir=/app/chrome-data --no-sandbox --disable-gpu &

# Ejecutar el script de Python
python /app/send_message.py
