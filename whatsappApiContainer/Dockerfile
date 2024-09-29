# Usar imagen base ligera de Python
FROM python:3.9-slim

# Establecer variables ARG para la arquitectura en tiempo de construcción
ARG TARGETPLATFORM
ARG TARGETARCH
ARG TARGETOS

# Instalar dependencias necesarias en una sola capa
RUN apt-get update && apt-get install -y --no-install-recommends \
    firefox-esr \
    wget \
    xvfb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Descargar e instalar Geckodriver según la arquitectura
RUN case "$TARGETARCH" in \
      "amd64") echo "Descargando geckodriver para amd64" && \
               wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz ;; \
      "arm64") echo "Descargando geckodriver para arm64" && \
               wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux-aarch64.tar.gz -O /tmp/geckodriver.tar.gz ;; \
      *) echo "Arquitectura no soportada: $TARGETARCH" && exit 1 ;; \
    esac && \
    tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm /tmp/geckodriver.tar.gz

# Instalar Selenium en una capa independiente
RUN pip install --no-cache-dir selenium

# Crear directorios necesarios
RUN mkdir -p /app/{screenshots,scripts,firefox_profile}

# Establecer el directorio de trabajo
WORKDIR /app/scripts

# Definir una variable de entorno para el perfil de Firefox
ENV FIREFOX_PROFILE_DIR=/data/firefox

# Añadir el script de Python al contenedor (se activa cuando copies los scripts)
# COPY ./scripts/enviar_mensaje.py /app/scripts/enviar_mensaje.py

# Definir volúmenes para datos persistentes
VOLUME /app/screenshots /app/scripts /data/firefox

# Definir el comando por defecto para ejecutar el script
CMD ["python", "/app/scripts/enviar_mensaje.py"]
