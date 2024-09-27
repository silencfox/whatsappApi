# whatsappApi

docker build -t whatsapp-sender .


docker run -d -it --rm \
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer2/capturas:/app/capturas \
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer2/cache:/app/cache \
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer2/scripts:/app/scripts \
whatsapp-sender



docker run -d -it --rm `
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer2/capturas:/app/capturas `
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer2/cache:/app/cache `
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer2/scripts:/app/scripts `
whatsapp-sender



docker build -t whatsapp-bot .


docker run -it -d -v D:/proyectos/Python/whatsappApi/whatsappapicontainer2/capturas:/app/screenshots whatsapp-bot:latest /bin/bash
