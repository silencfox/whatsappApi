docker rm whatsapp-bot
docker build -t whatsapp-bot -f Dockerfile .


docker run -d -it --rm --name whatsapp-bot `
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer2/screenshots:/app/screenshots `
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer2/scripts:/app/scripts `
-v D:/proyectos/Python/whatsappApi/whatsappapicontainer2/data/firefox:/app/firefox_profile `
whatsapp-bot /bin/bash

docker exec -it whatsapp-bot /bin/bash
