from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Configuración de Selenium y Chrome en modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# Configurar ruta para guardar las capturas de pantalla
screenshot_dir = "/app/screenshots/"

# Inicia el navegador Chrome en modo headless
driver = webdriver.Chrome(options=chrome_options)

# Abre Google y realiza una búsqueda de 'amor'
#driver.get("https://www.google.com")
#search_box = driver.find_element("name", "q")
#search_box.send_keys("amor")
#search_box.send_keys(Keys.RETURN)

driver.get("https://web.whatsapp.com/")


# Espera un momento para cargar la página de resultados
time.sleep(3)

# Toma una captura de pantalla de los resultados de búsqueda
driver.save_screenshot(screenshot_dir + "search_results.png")

# Cierra el navegador
driver.quit()
