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
output_folder = "/app/screenshots"
#target = '"DK Internacional"'
target = '"Notas"'
contact_path = f'//span[contains(@title,{target})]'
message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]'


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

def capturaPantalla(cap_name):
    # Capturar la pantalla después de seleccionar el destinatario
    screenshot_path = f"{output_folder}/{cap_name}.png"
    driver.save_screenshot(screenshot_path)
    print(f"captura {screenshot_path}")

# Esperar hasta que se cargue completamente la página de WhatsApp Web (hasta que aparezca un elemento principal)
try:
    # Esperamos hasta que aparezca el código QR o el menú principal
    WebDriverWait(driver, 40).until(
        EC.any_of(
            EC.presence_of_element_located((By.CSS_SELECTOR, "canvas")),  # Código QR
            #EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Cargando tus chats')]"))  # Mensaje de carga de chats
            EC.presence_of_element_located((By.XPATH, contact_path))  # Mensaje de carga de chats
            #By.CSS_SELECTOR, "div[data-testid='pane-side']"
        )
    )

    while driver.find_elements(By.CSS_SELECTOR, "canvas"):
        capturaPantalla("QR")
        print("Se detectó el código QR o el menú principal de WhatsApp.")
        print("Favor escanear el codigo para proceder")
        time.sleep(15)  # Esperar un tiempo antes de volver a verificar

    # Verificar qué evento ocurrió
    
    if driver.find_elements(By.XPATH, contact_path):
        print("Contacto detectado detectado.")
    elif driver.find_elements(By.CSS_SELECTOR, "div[data-testid='chat-list']"):
        print("Menú principal de WhatsApp detectado.")
    else :
        print("No se detecto ningun evento.")

except Exception as e:
    print("No se detectó el código QR ni el menú principal a tiempo:", e)
    driver.quit()



# Continuar con las acciones si no hay código QR o si ya se escaneó

# Definir el contacto y buscar el elemento por su título
contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_path)))
contact.click()

# Capturar la pantalla después de seleccionar el destinatario
capturaPantalla("Destinatario")

# Buscar el campo de mensaje usando XPath
# Usar ActionChains para enviar el mensaje

def EnviarMsg(message_box_path, msg):
    message_box = wait.until(EC.presence_of_element_located((By.XPATH, message_box_path)))
    actions = ActionChains(driver)
    actions.move_to_element(message_box)
    actions.click()
    actions.send_keys(msg)
    actions.send_keys(Keys.ENTER)
    actions.perform()  # Ejecutar la cadena de acciones

    # Capturar la pantalla después de enviar el mensaje
    capturaPantalla("MsgEnviado")

EnviarMsg(message_box_path, "Hola Mundo")


# Cerrar el navegador
time.sleep(15)
driver.quit()
