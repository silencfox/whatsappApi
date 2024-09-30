# whatsappApi

cls

docker rm whatsapp-bot

# Windows
docker build -t whatsapp-bot -f Dockerfile .


docker run -d -it --rm --name whatsapp-bot `
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer/screenshots:/app/screenshots `
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer/scripts:/app/scripts `
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer/data/firefox:/app/firefox_profile `
whatsapp-bot /bin/bash

docker exec -it whatsapp-bot /bin/bash


## linux 
docker build -t whatsapp-bot -f DockerfileARM .

docker run -d -it --rm --name whatsapp-bot \
-v ./screenshots:/app/screenshots \
-v ./scripts:/app/scripts \
-v ./data/firefox:/app/firefox_profile \
whatsapp-bot /bin/bash
docker exec -it whatsapp-bot /bin/bash

#RUN curl https://sh.rustup.rs -sSf | sh
#RUN cargo install geckodriver


# Navega a tu directorio de proyecto
d:
cd D:\proyectos\Python\whatsappApi\whatsappapicontainer2

# Crea un entorno virtual
python -m venv env

# Activa el entorno virtual
# Windows
.\env\Scripts\Activate

# Linux 
source nombre_entorno/bin/activate

# Instala un paquete, por ejemplo, requests
pip install -r requirements.txt

# Desactiva el entorno virtual cuando hayas terminado
deactivate
