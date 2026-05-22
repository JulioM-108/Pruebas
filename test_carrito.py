from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://www.demoblaze.com"
USUARIO = "testuser20251"
PASSWORD = "test1234"


def crear_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def hacer_login(driver, wait):
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
        assert False, f"Login falló. Mensaje: {mensaje}"
    except Exception as e:
        if "Login falló" in str(e):
            raise

    wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))


def agregar_primer_producto(driver, wait):
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//div[@class='card-block']//h4/a)[1]")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Add to cart']")
    )).click()

    wait.until(EC.alert_is_present()).accept()
    time.sleep(1)



# TEST 8: Agregar producto al carrito

def test_agregar_producto_al_carrito():
    driver = crear_driver()
    wait = WebDriverWait(driver, 20)

    hacer_login(driver, wait)
    agregar_primer_producto(driver, wait)

    wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "success")))

    items = driver.find_elements(By.CLASS_NAME, "success")
    assert len(items) > 0, "El carrito está vacío, no se agregó el producto"
    print(f"Productos en carrito: {len(items)}")
    driver.quit()



# TEST 9: Verificar total del carrito

def test_total_carrito():
    driver = crear_driver()
    wait = WebDriverWait(driver, 20)

    hacer_login(driver, wait)
    agregar_primer_producto(driver, wait)

    wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()
    time.sleep(2)

    total = wait.until(EC.presence_of_element_located((By.ID, "totalp"))).text

    assert total != "", "El total del carrito está vacío"
    assert int(total) > 0, f"El total debe ser mayor a 0, se obtuvo: {total}"
    print(f"Total del carrito: ${total}")
    driver.quit()



# TEST 10: Eliminar producto del carrito

def test_eliminar_producto_del_carrito():
    driver = crear_driver()
    wait = WebDriverWait(driver, 20)

    hacer_login(driver, wait)
    agregar_primer_producto(driver, wait)

    wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "success")))

    items_antes = driver.find_elements(By.CLASS_NAME, "success")
    assert len(items_antes) > 0, "No hay productos en el carrito para eliminar"

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//a[normalize-space()='Delete'])[1]")
    )).click()

    time.sleep(2)

    items_despues = driver.find_elements(By.CLASS_NAME, "success")
    assert len(items_despues) < len(items_antes), "El producto no fue eliminado"
    print(f"Eliminado correctamente. Antes: {len(items_antes)}, Después: {len(items_despues)}")
    driver.quit()



# TEST 11: Completar orden de compra (Place Order)

def test_place_order():
    driver = crear_driver()
    wait = WebDriverWait(driver, 20)

    hacer_login(driver, wait)
    agregar_primer_producto(driver, wait)

    wait.until(EC.element_to_be_clickable((By.ID, "cartur"))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "success")))
    time.sleep(1)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Place Order']")
    )).click()

    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Sebastian Castro")
    driver.find_element(By.ID, "country").send_keys("Colombia")
    driver.find_element(By.ID, "city").send_keys("Cali")
    driver.find_element(By.ID, "card").send_keys("1234567890123456")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2025")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Purchase']")
    )).click()

    confirmacion = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "sweet-alert")
    ))

    texto = confirmacion.text
    assert "Thank you for your purchase" in texto, f"No apareció confirmación. Texto: '{texto}'"
    print(f"COMPRA EXITOSA: {texto}")

    driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()
    driver.quit()