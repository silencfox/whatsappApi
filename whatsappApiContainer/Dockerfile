# Base image
FROM python:3.10-slim

# Instalar dependencias
RUN apt-get update && apt-get install -y \
    xvfb \
    wget \
    x11-utils \
    #xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic \
    fonts-liberation \
    chromium \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Instalar pywhatkit
RUN pip install pywhatkit

# Crear un directorio para almacenar los datos del navegador
RUN mkdir -p /app/chrome-data

# Copiar el script de inicio
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Definir el punto de entrada
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Definir el volumen para persistencia
VOLUME /app/chrome-data
