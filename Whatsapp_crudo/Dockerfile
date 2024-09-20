FROM python:3.9-slim

# Instala dependencias del sistema
RUN apt-get update && \
    apt-get install -y \
    xvfb \
    x11vnc \
    python3-pyqt5 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libxkbcommon-x11-0 \
    libxcomposite1 \
    libxcursor1 \
    libxi6 \
    libxtst6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/files
WORKDIR /app/files

# Instala dependencias de Python
COPY requirements.txt /
RUN pip install --no-cache-dir -r /app/files/requirements.txt

# Copia el script al contenedor
COPY main.py /main.py

# Define el comando por defecto
CMD ["xvfb-run", "-a", "python", "/script.py"]
