from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import os

print("Welcome to python scripts WS Automate")
# Inicializar Selenium WebDriver
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--profile')
options.add_argument('/app/firefox_profile')
# Usar un directorio específico para el perfil de Firefox
profile_path = "/app/firefox_profile"
if not os.path.exists(profile_path):
    os.makedirs(profile_path)
print("1")



print("1.5")

# Verificar si Xvfb está corriendo y matarlo si es necesario
def stop_xvfb():
    os.system('pkill -f Xvfb')

# Detener Xvfb antes de iniciar
stop_xvfb()

# Usar Xvfb para emular pantalla
os.system('Xvfb :99 -screen 0 1024x768x16 &')
os.environ['DISPLAY'] = ':99'

driver = webdriver.Firefox(options=options)
print("2")

# Navegar a WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Esperando que se genere el código QR...")

print("3")

# Esperar a que cargue el código QR
time.sleep(40)
print("4")

# Capturar la pantalla del código QR
screenshot_path = "/app/screenshots/codigo_qr.png"
driver.save_screenshot(screenshot_path)
print(f"Captura de pantalla guardada en {screenshot_path}")

# Esperar para que el usuario escanee el código QR
print("Escanea el código QR desde la imagen capturada.")
time.sleep(50)
print("5")

# Capturar la pantalla después de escanear el código QR
screenshot_path = "/app/screenshots/escaneado.png"
driver.save_screenshot(screenshot_path)
print(f"Captura de pantalla guardada en {screenshot_path}")

# Capturar pantallas repetidamente
for i in range(15):
    screenshot_path = f"/app/screenshots/escaneado_{i+1}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Captura de pantalla guardada en {screenshot_path}")


    time.sleep(10)

# Opcional: continuar con el flujo de enviar un mensaje después de escanear el código QR

# Buscar el contacto con el que quieres hablar
search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
search_box.click()
search_box.send_keys('Mi Morenita 2')
search_box.send_keys(Keys.ENTER)

# Enviar mensaje
message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='6']")
message_box.click()
message_box.send_keys('Hola, Linda.')
message_box.send_keys(Keys.ENTER)

# Cerrar el navegador
time.sleep(5)
driver.quit()
