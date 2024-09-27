FROM python:3.9-slim

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Instalar geckodriver para Firefox
#RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz \
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz \
    && tar -xvzf geckodriver-v0.35.0-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/geckodriver

WORKDIR /app/scripts

# Instalar Selenium
RUN pip install selenium

RUN mkdir -p /app/screenshots
RUN mkdir -p /app/scripts
RUN mkdir -p /app/cache
RUN mkdir -p /data/firefox

ENV FIREFOX_PROFILE_DIR=/data/firefox

# Añadir el script de Python al contenedor
#COPY ./scripts/enviar_mensaje.py /app/enviar_mensaje.py

# Definir un volumen para guardar capturas de pantalla
VOLUME /app/screenshots
VOLUME /app/scripts
VOLUME /app/cache
VOLUME /data/firefox
# Ejecutar el script
CMD ["python", "/app/enviar_mensaje.py"]
