# Etapa 1: Construcción de dependencias
FROM python:3.9-slim AS builder

# Establecer variables ARG para la arquitectura en tiempo de construcción
ARG TARGETPLATFORM
ARG TARGETARCH
ARG TARGETOS

# Instalar dependencias necesarias solo para construcción
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
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

# Instalar Selenium solo en la etapa de construcción
RUN pip install --no-cache-dir selenium

# Etapa 2: Imagen final
FROM python:3.9-slim

# Establecer variables ARG para la arquitectura en tiempo de construcción
ARG TARGETPLATFORM
ARG TARGETARCH
ARG TARGETOS

# Instalar Firefox y Xvfb en la imagen final
RUN apt-get update && apt-get install -y --no-install-recommends \
    firefox-esr \
    xvfb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiar Geckodriver desde la etapa de construcción
COPY --from=builder /usr/local/bin/geckodriver /usr/local/bin/geckodriver

# Instalar Selenium en la imagen final desde el builder
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Crear directorios necesarios
RUN mkdir -p /app/{screenshots,scripts,firefox_profile}

# Establecer el directorio de trabajo
WORKDIR /app/scripts

# Definir una variable de entorno para el perfil de Firefox
ENV FIREFOX_PROFILE_DIR=/data/firefox

# Añadir el script de Python al contenedor (se activa cuando copies los scripts)
# COPY ./scripts/enviar_mensaje.py /app/scripts/enviar_mensaje.py

# Definir volúmenes para persistencia de datos
VOLUME /app/screenshots /app/scripts /data/firefox

# Comando por defecto para ejecutar el script
CMD ["python", "/app/scripts/enviar_mensaje.py"]
