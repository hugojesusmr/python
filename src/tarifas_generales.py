#Esta librería permite interactuar con los navegadores web y simular acciones que un usuario podría realizar en un sitio web,
# como hacer clic en botones, llenar formularios y navegar por páginas
from selenium import webdriver
#Esta clase proporciona diferentes estrategias para localizar elementos en una página web.
from selenium.webdriver.common.by import By
#Esta clase se utiliza para interactuar con elementos de selección en formularios web, como menús desplegables
from selenium.webdriver.support.select import Select
#Esta clase se utiliza para configurar opciones específicas para un navegador controlado por Selenium.
from selenium.webdriver.chrome.options import Options

import tkinter as tk

#Almacenar las tarifas generales
esquema_tarifas = {}

#Ubicacion del navegar web
chromium_path='selenium\chrome-win64'
#Se crea una instancia de la clase Options de Selenium, que se utiliza para configurar opciones específicas para el controlador del navegador.
options= Options()
# representa la ubicación del archivo ejecutable del navegador Chromium
options.binary_location=chromium_path
#solucionar problemas de rendimiento o incompatibilidades en la automatización del navegador.
options.add_argument('--disable-dev-shm-usage')
#Ejecuta el navegador sin un sandbox, esto se relaciona con la seguridad y puede ser necesario en ciertos entornos.
options.add_argument("--no-sandbox")
#Ejecuta el navegador en modo sin cabeza, lo que significa que el navegador no se mostrará en la pantalla y funcionará en segundo plano.
options.add_argument("--headless")
#se crea una instancia del controlador del navegador Chrome utilizando las opciones configuradas. Esta instancia de webdriver se asigna al atributo self.driver, 
#lo que significa que estará disponible en todos los métodos de prueba dentro de la clase.
driver = webdriver.Chrome(options)

driver.get('https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRENegocio/Negocio.aspx')


                           
my_elements = driver.find_elements(By.PARTIAL_LINK_TEXT, 'T')
for element in my_elements:
    esquema_tarifas[element.get_attribute("href")]=element.text

print(esquema_tarifas[0])

driver.quit()

