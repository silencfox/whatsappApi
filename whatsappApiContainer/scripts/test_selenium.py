from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
import time
import os

# Configurar ruta para guardar las capturas de pantalla
screenshot_dir = "/app/screenshots/"
os.makedirs(screenshot_dir, exist_ok=True)

def search_in_google(browser_name, search_term):
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "chromium":
        chrome_options = ChromeOptions()
        chrome_options.binary_location = "/usr/bin/chromium"  # Ruta al binario de Chromium
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":

        # Define the path to your Firefox profile
        firefox_profile_path = "/data/firefox"
        
        firefox_options = FirefoxOptions()

        # Set up the Firefox profile and add it to options
        firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_path)

        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)

    else:
        raise ValueError("Navegador no soportado: " + browser_name)

    try:
        # Abre Google
        #driver.get("https://www.google.com")
        driver.get("https://web.whatsapp.com/")
        
        time.sleep(20)  # Espera para asegurar la carga de la página

        # Toma una captura de pantalla de la página principal de Google
        driver.save_screenshot(screenshot_dir + f"{browser_name}_google_home.png")

        # Encuentra el cuadro de búsqueda, escribe el término y presiona Enter
        #search_box = driver.find_element("name", "q")
        #search_box.send_keys(search_term)
        #search_box.send_keys(Keys.RETURN)

        # Espera un momento para cargar la página de resultados
        time.sleep(20)

        # Toma una captura de pantalla de los resultados de búsqueda
        driver.save_screenshot(screenshot_dir + f"{browser_name}_search_results.png")
        time.sleep(30)
        driver.save_screenshot(screenshot_dir + f"{browser_name}_search_results.png")
        time.sleep(30)
        driver.save_screenshot(screenshot_dir + f"{browser_name}_search_results.png")
        time.sleep(30)


    finally:
        # Cierra el navegador
        driver.quit()

# Realiza la búsqueda en cada navegador
search_term = "amor"
#for browser in ["chrome", "chromium", "firefox"]:
for browser in ["firefox"]:
    search_in_google(browser, search_term)
