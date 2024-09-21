from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configurar Selenium para que se conecte al contenedor
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Conectar al Selenium remoto
driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    options=chrome_options
)

try:
    # Abrir google.com
    driver.get("https://www.google.com")
    
    # Buscar la palabra "amor"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("amor")
    search_box.send_keys(Keys.RETURN)
    
    # Esperar unos segundos para cargar los resultados
    time.sleep(2)

    # Capturar un screenshot
    driver.save_screenshot("/usr/src/app/results/google_search_amor.png")
    print("Screenshot guardado exitosamente.")
finally:
    driver.quit()
