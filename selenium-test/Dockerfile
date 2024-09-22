FROM python:3.9-slim

# Instala dependencias de sistema
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    xvfb \
    chromium-driver \
    libnss3 \
    libgconf-2-4 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN echo "America/Santo_Domingo" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata


# Establece el directorio de trabajo
WORKDIR /app/scripts

# Instala las dependencias de Python
COPY requirements.txt .

RUN python --version \
    python -m venv venv
## crear entorno env en windows    
##RUN venv\Scripts\activate
## crear entorno env en linux    
RUN source venv/bin/activate

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt

# Copia el archivo de prueba en el contenedor
#COPY test_selenium.py /app/scripts/test_selenium.py

# Crea el directorio para las capturas de pantalla
RUN mkdir -p /app/screenshots



# Ejecuta el script de pruebas
#CMD ["python", "test_selenium.py"]
CMD ["/bin/bash"]
