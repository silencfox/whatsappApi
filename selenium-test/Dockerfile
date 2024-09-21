FROM python:3.9-slim

# Instala dependencias de sistema
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    xvfb \
    chromium-driver \
    libnss3 \
    libgconf-2-4 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el archivo de prueba en el contenedor
#COPY test_selenium.py /app/scripts/test_selenium.py

# Crea el directorio para las capturas de pantalla
RUN mkdir -p /app/screenshots

# Establece el directorio de trabajo
WORKDIR /app/scripts

# Ejecuta el script de pruebas
CMD ["python", "test_selenium.py"]
