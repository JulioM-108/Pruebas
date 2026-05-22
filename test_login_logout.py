from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

USUARIO = "testuser20251"
PASSWORD = "test1234"
URL = "https://www.demoblaze.com"


def crear_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver



# TEST 1: Login exitoso

def test_login_exitoso():
    driver = crear_driver()
    wait = WebDriverWait(driver, 20)

    driver.get(URL)
    wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

    campo_usuario = wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
    campo_usuario.clear()
    campo_usuario.send_keys(USUARIO)

    campo_password = driver.find_element(By.ID, "loginpassword")
    campo_password.clear()
    campo_password.send_keys(PASSWORD)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Log in']")
    )).click()

    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        mensaje = alert.text
        alert.accept()
        driver.quit()
        assert False, f"Login falló. Mensaje: {mensaje}"
    except Exception as e:
        if "Login falló" in str(e):
            raise

    wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
    nombre = driver.find_element(By.ID, "nameofuser").text

    assert "Welcome" in nombre, f"Texto encontrado: '{nombre}'"
    print(f"LOGIN EXITOSO: {nombre}")
    driver.quit()



# TEST 2: Login con contraseña incorrecta

def test_login_credenciales_invalidas():
    driver = crear_driver()
    wait = WebDriverWait(driver, 20)

    driver.get(URL)
    wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

    campo_usuario = wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
    campo_usuario.clear()
    campo_usuario.send_keys(USUARIO)

    campo_password = driver.find_element(By.ID, "loginpassword")
    campo_password.clear()
    campo_password.send_keys("contrasena_incorrecta")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Log in']")
    )).click()

    alert = WebDriverWait(driver, 8).until(EC.alert_is_present())
    mensaje = alert.text
    alert.accept()

    assert len(mensaje) > 0, "Se esperaba una alerta de error"
    print(f"PRUEBA CORRECTA - Alerta recibida: {mensaje}")
    driver.quit()



# TEST 3: Logout exitoso

def test_logout_exitoso():
    driver = crear_driver()
    wait = WebDriverWait(driver, 20)

    # Login
    driver.get(URL)
    wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()

    campo_usuario = wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
    campo_usuario.clear()
    campo_usuario.send_keys(USUARIO)

    campo_password = driver.find_element(By.ID, "loginpassword")
    campo_password.clear()
    campo_password.send_keys(PASSWORD)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Log in']")
    )).click()

    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        mensaje = alert.text
        alert.accept()
        driver.quit()
        assert False, f"Login falló. Mensaje: {mensaje}"
    except Exception as e:
        if "Login falló" in str(e):
            raise

    wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))

    # Logout
    wait.until(EC.element_to_be_clickable((By.ID, "logout2"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "login2")))

    assert driver.find_element(By.ID, "login2").is_displayed()
    print("LOGOUT EXITOSO")
    driver.quit()