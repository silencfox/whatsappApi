import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

# Configuración inicial
PROFILE_PATH = "/app/firefox_profile"
OUTPUT_FOLDER = "/app/screenshots"
TARGET_CONTACT = '"Notas"'
CONTACT_PATH = f'//span[contains(@title,{TARGET_CONTACT})]'
MESSAGE_BOX_PATH = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]'

# Iniciar Xvfb para emulación de pantalla
def start_xvfb():
    if not os.environ.get('DISPLAY'):
        os.system('Xvfb :99 -screen 0 1024x768x16 &')
        os.environ['DISPLAY'] = ':99'

# Inicializar el WebDriver
def initialize_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--profile')
    options.add_argument(PROFILE_PATH)

    if not os.path.exists(PROFILE_PATH):
        os.makedirs(PROFILE_PATH)

    driver = webdriver.Firefox(options=options)
    return driver

# Capturar pantallas
def captura_pantalla(driver, cap_name):
    screenshot_path = f"{OUTPUT_FOLDER}/{cap_name}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Captura guardada: {screenshot_path}")

# Automatizar WhatsApp Web
def automate_whatsapp():
    start_xvfb()

    driver = initialize_driver()
    wait = WebDriverWait(driver, 60)

    try:
        # Navegar a WhatsApp Web
        driver.get("https://web.whatsapp.com")
        print("Esperando que la página cargue completamente...")

        # Esperar hasta que se cargue el código QR o el contacto
        WebDriverWait(driver, 40).until(
            EC.any_of(
                EC.presence_of_element_located((By.CSS_SELECTOR, "canvas")),  # Código QR
                EC.presence_of_element_located((By.XPATH, CONTACT_PATH))  # Carga de chats
            )
        )

        while driver.find_elements(By.CSS_SELECTOR, "canvas"):
            captura_pantalla(driver, "QR")
            print("Código QR detectado. Favor escanear el código para proceder.")
            time.sleep(15)

        contact = wait.until(EC.presence_of_element_located((By.XPATH, CONTACT_PATH)))
        contact.click()
        captura_pantalla(driver, "Destinatario")

        # Enviar un mensaje
        enviar_mensaje(driver, MESSAGE_BOX_PATH, "Hola desde Raspberry Pi")

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error: {e}")
    finally:
        time.sleep(15)
        driver.quit()

# Función para enviar mensajes
def enviar_mensaje(driver, message_box_path, msg):
    wait = WebDriverWait(driver, 10)
    message_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
    actions = ActionChains(driver)
    actions.move_to_element(message_box).click().send_keys(msg).send_keys(Keys.ENTER).perform()
    captura_pantalla(driver, "MensajeEnviado")

if __name__ == "__main__":
    print("Automatización WhatsApp iniciada...")
    automate_whatsapp()
