#Importar Libreria
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest import mark
import time


#Ejecucion del Webdriver
#driver = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window() # For maximizing window
driver.get("https://www.corotos.com.do/")


#Prueba de Button (Inicio de sesion)
@mark.ui
def test_pruebaButton():
    driver.find_element(By.ID, 'g4-taco-signin-button').click()
    driver.get_screenshot_as_file('C:\\Users\\cesar\\OneDrive\\Escritorio\\Prueba_SE\\screenshot\\prueba_button.png')
    assert True

#Prueba Inicio de sesion
@mark.data
def test_pruebaLogin():
    element_email = driver.find_element(By.ID, 'app_user_email')
    element_email.send_keys('prueba.testing20210672@gmail.com')

    element_password = driver.find_element(By.ID, 'app_user_password')
    element_password.send_keys('20210672' + Keys.ENTER)
    driver.get_screenshot_as_file('C:\\Users\\cesar\\OneDrive\\Escritorio\\Prueba_SE\\screenshot\\prueba_login.png')
    assert True

#Prueba del Buscador
@mark.ui
def test_pruebaSearch():
    driver.get("https://www.corotos.com.do/c/inmuebles")

    wait = WebDriverWait(driver, 5)

    search_bar = wait.until(EC.visibility_of_element_located((By.ID, 'search')))
    search_bar.send_keys('Mercedes Benz' + Keys.ENTER)

    driver.get_screenshot_as_file('C:\\Users\\cesar\\OneDrive\\Escritorio\\Prueba_SE\\screenshot\\prueba_search.png')
    assert True

#Prueba de logo
@mark.ui
def test_pruebaLogo():
    driver.get("https://www.corotos.com.do/k/Mercedes%20Benz")

    wait = WebDriverWait(driver, 5)

    logo_click = wait.until(EC.element_to_be_clickable((By.ID, 'g4-taco-corotos-logo')))
    logo_click.click()

    driver.get_screenshot_as_file('C:\\Users\\cesar\\OneDrive\\Escritorio\\Prueba_SE\\screenshot\\prueba_logo.png')
    assert True

#Prueba Button (Favoritos)
@mark.ui
def test_pruebaFavorites():
    driver.find_element(By.ID, 'g4-taco-favorites-navbar-button').click()
    driver.get_screenshot_as_file('C:\\Users\\cesar\\OneDrive\\Escritorio\\Prueba_SE\\screenshot\\prueba_buttonFavorites.png')
    assert True

#Prueba Sing out
@mark.ui
def test_pruebaSingOut():
    try:
        wait = WebDriverWait(driver, 5)
        singout_click = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Cerrar sesión')))
        singout_click.click()
        time.sleep(30)
    finally:
         driver.quit()
assert True