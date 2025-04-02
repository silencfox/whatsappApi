# Etapa 1: Construcción de dependencias
FROM python:3.9-slim AS builder

# Establecer variables ARG para la arquitectura en tiempo de construcción
ARG TARGETPLATFORM
ARG TARGETARCH
ARG TARGETOS

RUN mkdir -p /app
COPY ./requirements.txt /app/requirements.txt

# Instalar dependencias necesarias solo para construcción
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
	curl \ 
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*



# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y libaio1 unzip && rm -rf /var/lib/apt/lists/*

# Descargar e instalar Oracle Instant Client
## https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html
#RUN wget --no-check-certificate https://download.oracle.com/otn_software/linux/instantclient/2370000/instantclient-basiclite-linux.x64-23.7.0.25.01.zip 
RUN curl -k -o /tmp/instantclient.zip https://download.oracle.com/otn_software/linux/instantclient/2370000/instantclient-basiclite-linux.x64-23.7.0.25.01.zip && \
    unzip /tmp/instantclient.zip -d /opt/oracle && \
    rm /tmp/instantclient.zip && \
    ln -s /opt/oracle/instantclient_21_11 /opt/oracle/instantclient && \
    echo "/opt/oracle/instantclient" > /etc/ld.so.conf.d/oracle-instantclient.conf && \
    ldconfig

# Configurar variables de entorno para Oracle
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient
ENV ORACLE_HOME=/opt/oracle/instantclient
ENV PATH=$ORACLE_HOME:$PATH





# Descargar e instalar Geckodriver según la arquitectura
RUN case "$TARGETARCH" in \
      "amd64") echo "Descargando geckodriver para amd64" && \
               wget --no-check-certificate https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz ;; \
      "arm64") echo "Descargando geckodriver para arm64" && \
               wget --no-check-certificate https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux-aarch64.tar.gz -O /tmp/geckodriver.tar.gz ;; \
      *) echo "Arquitectura no soportada: $TARGETARCH" && exit 1 ;; \
    esac && \
    tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm /tmp/geckodriver.tar.gz

# Instalar Selenium solo en la etapa de construcción
RUN pip install --trusted-host github.com --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir -r /app/requirements.txt
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
 COPY ./scripts/enviar_mensaje.py /app/scripts/enviar_mensaje.py
# Copiar el script de conexión
COPY ./scripts/script.py /app/scripts/script.py

# Definir volúmenes para persistencia de datos
VOLUME /app/screenshots /app/scripts /data/firefox



# Comando por defecto para ejecutar el script
CMD ["python", "/app/scripts/enviar_mensaje.py"]
