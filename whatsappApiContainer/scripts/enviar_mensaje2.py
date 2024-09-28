from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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

# Verificar si Xvfb está corriendo y matarlo si es necesario
def stop_xvfb():
    os.system('pkill -f Xvfb')

# Detener Xvfb antes de iniciar
stop_xvfb()

# Usar Xvfb para emular pantalla
os.system('Xvfb :99 -screen 0 1024x768x16 &')
os.environ['DISPLAY'] = ':99'

# Iniciar el WebDriver
driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 600)

# Navegar a WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Esperando que la página cargue completamente...")

# Esperar hasta que se cargue completamente la página de WhatsApp Web (hasta que aparezca un elemento principal)
wait.until(EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!'] | //div[@id='pane-side']")))

# Verificar si existe el código QR en la página
try:
    qr_code = driver.find_element(By.XPATH, "//canvas[@aria-label='Scan me!']")
    print("Código QR encontrado. Capturando pantalla...")
    
    # Capturar la pantalla del código QR
    screenshot_path = "/app/screenshots/codigo_qr.png"
    driver.save_screenshot(screenshot_path)
    print(f"Escanea el código QR desde la imagen capturada en {screenshot_path}")
    
    # Esperar para que el usuario escanee el código QR
    time.sleep(40)

except Exception as e:
    print("No se encontró código QR. Continuando con el flujo...")

# Continuar con las acciones si no hay código QR o si ya se escaneó

# Definir el contacto y buscar el elemento por su título
target = '"DK Internacional"'
contact_path = f'//span[contains(@title,{target})]'
contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
contact.click()

# Capturar la pantalla después de seleccionar el destinatario
screenshot_path = "/app/screenshots/Destinatario.png"
driver.save_screenshot(screenshot_path)
print(f"Destinatario {screenshot_path}")

# Buscar el campo de mensaje usando XPath
message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]'
message_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))

# Usar ActionChains para enviar el mensaje
actions = ActionChains(driver)
actions.move_to_element(message_box)
actions.click()
actions.send_keys("successful")
actions.send_keys(Keys.ENTER)
actions.perform()  # Ejecutar la cadena de acciones

# Capturar la pantalla después de enviar el mensaje
screenshot_path = "/app/screenshots/MsgEnviado.png"
driver.save_screenshot(screenshot_path)
print(f"Mensaje Enviado {screenshot_path}")

# Cerrar el navegador
time.sleep(15)
driver.quit()
