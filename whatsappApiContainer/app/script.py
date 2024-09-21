import pywhatkit
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

# Función para enviar un mensaje con pywhatkit (puedes adaptarla según tu uso)
def send_message():
    # Envía un mensaje de prueba, asegúrate de que pywhatkit esté configurado con WhatsApp
    pywhatkit.sendwhatmsg_instantly("+123456789", "Mensaje de prueba")

# Configurar el navegador en modo headless
def open_browser_and_capture_screenshot(output_path):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Configurar Selenium con Chrome
    driver = webdriver.Chrome(options=chrome_options)
    
    # Abre la página web de WhatsApp o la URL que necesitas automatizar
    driver.get('https://web.whatsapp.com')

    # Espera para asegurar que la página cargue completamente
    time.sleep(10)  # Ajusta según el tiempo de carga esperado

    # Toma una captura de pantalla
    screenshot_path = f"{output_path}/screenshot.png"
    driver.save_screenshot(screenshot_path)

    # Cerrar el navegador
    driver.quit()

    # Verificar si la captura fue tomada correctamente
    img = Image.open(screenshot_path)
    img.show()

# Definir el path del volumen montado
output_path = "/app/screenshots"  # Ruta dentro del contenedor

# Llamar a las funciones
send_message()
open_browser_and_capture_screenshot(output_path)
