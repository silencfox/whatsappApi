from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Inicializar Selenium WebDriver
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Usar Xvfb para emular pantalla
os.system('Xvfb :99 -screen 0 1024x768x16 &')
os.environ['DISPLAY'] = ':99'

driver = webdriver.Firefox(options=options)

# Navegar a WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Esperando que se genere el código QR...")

# Esperar a que cargue el código QR
time.sleep(40)

# Capturar la pantalla del código QR
screenshot_path = "/app/screenshots/codigo_qr.png"
driver.save_screenshot(screenshot_path)
print(f"Captura de pantalla guardada en {screenshot_path}")

# Ahora puedes abrir la captura desde el volumen compartido y escanear el código QR
print("Escanea el código QR desde la imagen capturada.")

# Esperar para que el usuario escanee el código QR
time.sleep(50)

# Capturar la pantalla del código QR
screenshot_path = "/app/screenshots/escaneado.png"
driver.save_screenshot(screenshot_path)
print(f"Captura de pantalla guardada en {screenshot_path}")

# Esperar para que el usuario escanee el código QR
time.sleep(40)

# Capturar la pantalla del código QR
screenshot_path = "/app/screenshots/escaneado1.png"
driver.save_screenshot(screenshot_path)
print(f"Captura de pantalla guardada en {screenshot_path}")



# Suponiendo que `driver` ya está definido y configurado
for i in range(10):
    # Capturar la pantalla del código QR
    screenshot_path = f"/app/screenshots/escaneado_{i+1}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Captura de pantalla guardada en {screenshot_path}")
    
    # Esperar 10 segundos antes de la próxima iteración
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
message_box.send_keys('Hola, este es un mensaje automatizado.')
message_box.send_keys(Keys.ENTER)

# Cerrar el navegador
time.sleep(5)
driver.quit()
