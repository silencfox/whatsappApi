FROM python:3.9-slim

# Establece una variable ARG para detectar la arquitectura en tiempo de construcción
ARG TARGETPLATFORM
ARG TARGETARCH
ARG TARGETOS

# Ejecuta diferentes comandos según la arquitectura
RUN echo "Sistema operativo: $TARGETOS, Arquitectura: $TARGETARCH, Plataforma: $TARGETPLATFORM"


# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Instalar geckodriver para Firefox
# Ejecuta diferentes comandos según la arquitectura
# Detecta la arquitectura y descarga el geckodriver adecuado

RUN if [ "$TARGETARCH" = "amd64" ]; then \
        echo "Descargando geckodriver para amd64"; \
        wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz -O geckodriver-v0.35.0-linux.tar.gz; \
    elif [ "$TARGETARCH" = "arm64" ]; then \
        echo "Descargando geckodriver para arm64"; \
        wget https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux-aarch64.tar.gz -O geckodriver-v0.35.0-linux.tar.gz; \
    else \
        echo "Arquitectura no soportada: $TARGETARCH"; \
        exit 1; \
    fi && \
        tar -xvzf geckodriver-v0.35.0-linux*.tar.gz && \
        mv geckodriver /usr/local/bin/ && \
        chmod +x /usr/local/bin/geckodriver

# Limpieza de archivos innecesarios
RUN rm geckodriver-v0.35.0-linux*.tar.gz


# Instalar Selenium
RUN pip install selenium 

RUN mkdir -p /app/screenshots
RUN mkdir -p /app/scripts
RUN mkdir -p /app/firefox_profile


WORKDIR /app/scripts

ENV FIREFOX_PROFILE_DIR=/data/firefox

# Añadir el script de Python al contenedor
#COPY ./scripts/enviar_mensaje.py /app/enviar_mensaje.py

# Definir un volumen para guardar capturas de pantalla
VOLUME /app/screenshots
VOLUME /app/scripts
VOLUME /data/firefox
# Ejecutar el script
#CMD ["python", "/app/scripts/enviar_mensaje.py"]
CMD ["/bin/bash"]
