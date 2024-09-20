import pywhatkit as kit
import time

# Enviar un mensaje de prueba
kit.sendwhatmsg_instantly("+18493504723", "Hola, este es un mensaje de prueba desde Docker")

# Pausa para dar tiempo a la carga de WhatsApp Web
time.sleep(20)
