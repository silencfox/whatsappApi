import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Obtener la ruta para guardar las capturas de pantalla
screenshots_dir = os.getenv('SCREENSHOTS_DIR', '/screenshots')

# Configurar Chrome headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# Configurar el servicio para chromedriver
service = Service("/usr/local/bin/chromedriver")

# Crear el driver de Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Abrir Google
    driver.get("https://www.google.com")

    # Buscar la palabra 'amor'
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("amor")
    search_box.send_keys(Keys.RETURN)

    # Esperar un poco para que carguen los resultados
    time.sleep(3)

    # Capturar una captura de pantalla de los resultados
    screenshot_path = os.path.join(screenshots_dir, "search_results.png")
    driver.save_screenshot(screenshot_path)
    print(f"Captura de pantalla guardada en: {screenshot_path}")

finally:
    # Cerrar el navegador
    driver.quit()
