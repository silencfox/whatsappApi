# whatsappApi


# Navega a tu directorio de proyecto
d:
cd D:\proyectos\Python\whatsappApi\whatsappapicontainer2

# Crea un entorno virtual
python -m venv env

# Activa el entorno virtual
# Windows
.\env\Scripts\Activate
# venv\Scripts\activate.bat
# venv\Scripts\Activate.ps1

# Linux 
source nombre_entorno/bin/activate

# Instala un paquete, por ejemplo, requests
pip install -r requirements.txt

# Desactiva el entorno virtual cuando hayas terminado
deactivate



cls

docker rm whatsapp-bot
docker build -t whatsapp-bot -f Dockerfile .


## Windows
docker run -d -it --rm --name whatsapp-bot `
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer/screenshots:/app/screenshots `
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer/scripts:/app/scripts `
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer/data/firefox:/app/firefox_profile `
whatsapp-bot /bin/bash

## Linux
docker run -d -it --rm --name whatsapp-bot \
-v ./screenshots:/app/screenshots \
-v ./scripts:/app/scripts \
-v ./data/firefox:/app/firefox_profile \
whatsapp-bot /bin/bash

docker exec -it whatsapp-bot /bin/bash
