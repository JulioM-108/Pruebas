from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://www.demoblaze.com"


def crear_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


# TEST 4: Filtrado por categoría Phones

def test_filtro_categoria_phones():
    driver = crear_driver()
    wait = WebDriverWait(driver, 20)

    driver.get(URL)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Phones']")
    )).click()

    time.sleep(2)

    productos = wait.until(EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "card-title")
    ))
    nombres = [p.text for p in productos if p.text.strip()]

    assert len(nombres) > 0, "No se encontraron productos en Phones"
    print(f"Productos en Phones ({len(nombres)}): {nombres}")
    driver.quit()



# TEST 5: Filtrado por categoría Laptops

def test_filtro_categoria_laptops():
    driver = crear_driver()
    wait = WebDriverWait(driver, 20)

    driver.get(URL)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Laptops']")
    )).click()

    time.sleep(2)

    productos = wait.until(EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "card-title")
    ))
    nombres = [p.text for p in productos if p.text.strip()]

    assert len(nombres) > 0, "No se encontraron productos en Laptops"
    print(f"Productos en Laptops ({len(nombres)}): {nombres}")
    driver.quit()



# TEST 6: Filtrado por categoría Monitors

def test_filtro_categoria_monitors():
    driver = crear_driver()
    wait = WebDriverWait(driver, 20)

    driver.get(URL)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Monitors']")
    )).click()

    time.sleep(2)

    productos = wait.until(EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "card-title")
    ))
    nombres = [p.text for p in productos if p.text.strip()]

    assert len(nombres) > 0, "No se encontraron productos en Monitors"
    print(f"Productos en Monitors ({len(nombres)}): {nombres}")
    driver.quit()



# TEST 7: Ver detalle de un producto

def test_detalle_producto():
    driver = crear_driver()
    wait = WebDriverWait(driver, 20)

    driver.get(URL)

    primer_producto = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//div[@class='card-block']//h4/a)[1]")
    ))
    primer_producto.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "name")))

    nombre = driver.find_element(By.CLASS_NAME, "name").text
    precio = driver.find_element(By.CLASS_NAME, "price-container").text

    assert len(nombre) > 0, "No se encontró el nombre del producto"
    assert len(precio) > 0, "No se encontró el precio del producto"

    print(f"Producto: {nombre} | Precio: {precio}")
    driver.quit()