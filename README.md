# 🧪 Automatización de Pruebas — DemoBlaze Product Store

Proyecto de automatización de pruebas funcionales para la aplicación web [DemoBlaze](https://www.demoblaze.com), desarrollado con **Selenium WebDriver**, **Python** y **Pytest**.

---

## 📋 Descripción

Este proyecto implementa pruebas automatizadas de tipo **funcional/end-to-end** sobre los módulos principales de DemoBlaze, una tienda de e-commerce demo. Las pruebas simulan el comportamiento real de un usuario en el navegador: iniciar sesión, navegar por el catálogo, agregar productos al carrito y completar una orden de compra.

Las pruebas fueron desarrolladas como parte de un plan de pruebas formal que incluye estrategia de automatización, selección y justificación de herramientas, ejecución y reporte de resultados.

---

## 🛠️ Tecnologías utilizadas

| Herramienta | Versión | Propósito |
|---|---|---|
| Python | 3.13 | Lenguaje de programación |
| Selenium WebDriver | Latest | Automatización del navegador |
| ChromeDriver | Auto (webdriver-manager) | Traductor entre Selenium y Chrome |
| Pytest | 9.0.3 | Framework de ejecución de pruebas |
| pytest-html | 4.2.0 | Generación de reportes HTML |
| webdriver-manager | Latest | Gestión automática de ChromeDriver |

---

## 🔗 Cómo funciona la automatización

```
Tu código Python
      │
      ▼
Selenium WebDriver  →  convierte instrucciones en peticiones HTTP (protocolo WebDriver)
      │
      ▼
ChromeDriver.exe    →  traduce las peticiones a comandos internos de Chrome
      │
      ▼
Google Chrome       →  ejecuta las acciones reales en pantalla
```

- **WebDriver** es el protocolo estándar W3C que define cómo comunicarse con un navegador.
- **Selenium WebDriver** es la librería Python que implementa ese protocolo.
- **ChromeDriver** es el ejecutable que hace de puente entre Selenium y Chrome. Debe tener la misma versión que Chrome instalado. Por eso se usa `webdriver-manager`, que lo descarga automáticamente.
- **Pytest** organiza, ejecuta y reporta los resultados de cada función `test_`.

---

## 📁 Estructura del proyecto

```
Demo-Test/
├── test_login.py        # Pruebas de inicio de sesión con credenciales válidas e inválidas
├── test_logout.py       # Prueba de cierre de sesión
├── test_catalogo.py     # Pruebas de filtrado por categoría y detalle de producto
├── test_carrito.py      # Pruebas de carrito: agregar, eliminar, total y Place Order
├── requirements.txt     # Dependencias del proyecto
└── README.md
```

---

## 🧩 Casos de prueba automatizados

| # | Archivo | Caso de prueba |
|---|---|---|
| 1 | test_login.py | Login exitoso con credenciales válidas |
| 2 | test_login.py | Login fallido con contraseña incorrecta |
| 3 | test_logout.py | Logout exitoso |
| 4 | test_catalogo.py | Filtrado por categoría Phones |
| 5 | test_catalogo.py | Filtrado por categoría Laptops |
| 6 | test_catalogo.py | Filtrado por categoría Monitors |
| 7 | test_catalogo.py | Ver detalle de producto |
| 8 | test_carrito.py | Agregar producto al carrito |
| 9 | test_carrito.py | Verificar total del carrito |
| 10 | test_carrito.py | Eliminar producto del carrito |
| 11 | test_carrito.py | Completar orden de compra (Place Order) |

---

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Crear entorno virtual

```bash
python -m venv env
```

Activar en Windows:
```bash
env\Scripts\activate
```

Activar en Mac/Linux:
```bash
source env/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear cuenta de prueba

Antes de ejecutar las pruebas, registrar manualmente una cuenta en [demoblaze.com](https://www.demoblaze.com) con:
- **Usuario:** `testuser20251`
- **Contraseña:** `test1234`

---

## ▶️ Ejecución de pruebas

### Correr un archivo específico

```bash
pytest test_login.py -v -s
pytest test_logout.py -v -s
pytest test_catalogo.py -v -s
pytest test_carrito.py -v -s
```

### Correr todas las pruebas y generar reporte HTML

```bash
pytest test_login.py test_logout.py test_catalogo.py test_carrito.py -v -s --html=reporte.html --self-contained-html
```

El reporte queda guardado como `reporte.html` en la carpeta del proyecto.

## 👥 Equipo

- Sebastian Castro Obando
- Julio Mazo Reyes
