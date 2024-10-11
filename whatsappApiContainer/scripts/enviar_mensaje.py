import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Asegúrate de que esta línea esté presente
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Configuración inicial
PROFILE_PATH = "/app/firefox_profile"
OUTPUT_FOLDER = "/app/screenshots"
TARGET_CONTACT = '"Notas"'
CONTACT_PATH = f'//span[contains(@title,{TARGET_CONTACT})]'
MESSAGE_BOX_PATH = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]'

# Inicializar Selenium WebDriver
def initialize_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--profile')
    options.add_argument(PROFILE_PATH)

    # Verificar y crear el directorio del perfil
    if not os.path.exists(PROFILE_PATH):
        os.makedirs(PROFILE_PATH)

    # Iniciar el WebDriver
    driver = webdriver.Firefox(options=options)
    return driver

# Función para detener Xvfb
def stop_xvfb():
    os.system('pkill -f Xvfb')

# Función para emular pantalla con Xvfb
def start_xvfb():
    os.system('Xvfb :99 -screen 0 1024x768x16 &')
    os.environ['DISPLAY'] = ':99'

# Captura de pantalla
def captura_pantalla(driver, cap_name):
    screenshot_path = f"{OUTPUT_FOLDER}/{cap_name}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Captura guardada: {screenshot_path}")

# Función principal para la automatización de WhatsApp
def automate_whatsapp():
    # Detener Xvfb y luego iniciarlo
    stop_xvfb()
    start_xvfb()

    driver = initialize_driver()
    wait = WebDriverWait(driver, 600)

    try:
        # Navegar a WhatsApp Web
        driver.get("https://web.whatsapp.com")
        print("Esperando que la página cargue completamente...")

        # Esperar hasta que se cargue el código QR o el contacto
        WebDriverWait(driver, 40).until(
            EC.any_of(
                EC.presence_of_element_located((By.CSS_SELECTOR, "canvas")),  # Código QR
                EC.presence_of_element_located((By.XPATH, CONTACT_PATH))  # Mensaje de carga de chats
            )
        )

        # Captura de pantalla y espera mientras esté visible el código QR
        while driver.find_elements(By.CSS_SELECTOR, "canvas"):
            captura_pantalla(driver, "QR")
            print("Código QR detectado. Favor escanear el código para proceder.")
            time.sleep(15)

        # Verificar qué evento ocurrió
        if driver.find_elements(By.XPATH, CONTACT_PATH):
            print("Contacto detectado.")
        else:
            print("No se detectó ningún evento.")

        # Seleccionar el contacto
        contact = wait.until(EC.presence_of_element_located((By.XPATH, CONTACT_PATH)))
        contact.click()
        captura_pantalla(driver, "Destinatario")

        # Enviar un mensaje
        enviar_mensaje(driver, MESSAGE_BOX_PATH, "Hola Mundo")


    except Exception as e:
        print("Error:", e)
    finally:
        # Cerrar el navegador
        time.sleep(15)
        driver.quit()

# Función para enviar un mensaje
def enviar_mensaje(driver, message_box_path, msg):
    wait = WebDriverWait(driver, 10)
    message_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
    actions = ActionChains(driver)
    actions.move_to_element(message_box).click().send_keys(msg).send_keys(Keys.ENTER).perform()
    time.sleep(25)
    captura_pantalla(driver, "MsgEnviado")

if __name__ == "__main__":
    print("Welcome to python scripts WS Automate")
    automate_whatsapp()
