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

#RUN add-apt-repository universe
#RUN add-apt-repository multiverse
#RUN apt update
#RUN apt install libvulkan1   

#RUN curl -LO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
#RUN rm google-chrome-stable_current_amd64.deb

# Instala las dependencias de Python
COPY requirements.txt .
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt

# Copia el archivo de prueba en el contenedor
#COPY test_selenium.py /app/scripts/test_selenium.py

# Crea el directorio para las capturas de pantalla
RUN mkdir -p /app/screenshots

# Establece el directorio de trabajo
WORKDIR /app/scripts

# Ejecuta el script de pruebas
#CMD ["python", "test_selenium.py"]
CMD ["/bin/bash"]
