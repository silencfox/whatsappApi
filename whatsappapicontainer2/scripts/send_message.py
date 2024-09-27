import pywhatkit
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os

# Configuración de directorios
screenshot_dir = "/app/capturas/"
cache_dir = "/app/cache/"
os.makedirs(screenshot_dir, exist_ok=True)
os.makedirs(cache_dir, exist_ok=True)

# Configuración de Firefox en modo headless con caché para la sesión
options = Options()
options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
#options.add_argument('--disable-gpu')
#options.add_argument('--window-size=1920x1080')

# Establecer la carpeta de caché para guardar la sesión
options.set_preference("browser.cache.disk.parent_directory", cache_dir)

# Crear instancia del navegador con las opciones
driver = webdriver.Firefox(options=options)

# Navegar a WhatsApp Web
driver.get('https://web.whatsapp.com')

# Verificar si la sesión ya está iniciada
try:
    # Si este selector está presente, la sesión está iniciada
    driver.find_element(By.CSS_SELECTOR, 'div._2dH1A')
    print("Sesión ya iniciada. Procediendo con el envío del mensaje.")
    # Enviar el mensaje con pywhatkit
    pywhatkit.sendwhatmsg_instantly("+1234567890", "Hola, este es un mensaje automatizado.")
except:
    print("Sesión no iniciada. Capturando código QR.")
    # Captura el código QR si la sesión no está iniciada
    driver.save_screenshot(screenshot_dir + "codigo_qr.png")
    # Espera 2 minutos para que el usuario escanee el código QR
    time.sleep(120)
    # Después de la espera, intenta enviar el mensaje
    pywhatkit.sendwhatmsg_instantly("+1234567890", "Hola, este es un mensaje automatizado.")

# Cierra el navegador
driver.quit()
