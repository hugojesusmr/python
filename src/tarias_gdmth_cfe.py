#Esta librería proporciona funciones para leer, escribir y trabajar con datos tabulares en formato CSV
import csv 
import os
#Esta librería proporciona funciones relacionadas con el tiempo
import time
import datetime
#Esta librería permite escribir y ejecutar pruebas unitarias para asegurarse de que las funciones y clases funcionen como se espera
import unittest
#Esta librería permite interactuar con los navegadores web y simular acciones que un usuario podría realizar en un sitio web,
# como hacer clic en botones, llenar formularios y navegar por páginas
from selenium import webdriver
#Esta clase proporciona diferentes estrategias para localizar elementos en una página web.
from selenium.webdriver.common.by import By
#Esta clase se utiliza para interactuar con elementos de selección en formularios web, como menús desplegables
from selenium.webdriver.support.select import Select
#Esta clase se utiliza para configurar opciones específicas para un navegador controlado por Selenium.
from selenium.webdriver.chrome.options import Options
from tkinter import filedialog
#La clase unittest.TestCase se utilizan para verificar si las condiciones en las pruebas son verdaderas y configurar el ambiente de Pruebas de cada prueba individual.
class usando_unittest(unittest.TestCase):
    #La función mide_tiempo es un decorador que toma como argumento otra función llamada funcion.
    #Dentro de mide_tiempo, se define una función anidada llamada funcion_medida que toma cualquier número de argumentos (*args)
    #  y argumentos de palabras clave (**kwargs) que la función original pueda recibir.
    def mide_tiempo(funcion):
        def funcion_medida(*args, **kwargs):
            inicio = time.time()   
            #Se llama a la función original (funcion(*args, **kwargs)) con los mismos argumentos y argumentos de palabras clave pasados a funcion_medida.
            c = funcion(*args, **kwargs) 
            #Después de que la función original haya terminado de ejecutarse, se calcula el tiempo transcurrido restando el tiempo de inicio del tiempo actual. 
            # Esto te da el tiempo que tomó ejecutar la función, se imprime el tiempo de ejecución calculado 
            print(time.time() - inicio)     
            return c
            # y se devuelve el resultado de la función original.
        return funcion_medida
    #El método setUp es un método especial en las clases de prueba de unittest.TestCase que se ejecuta antes de cada prueba definida en la clase.
    #Su propósito es configurar las condiciones necesarias para que las pruebas se ejecuten en un ambiente controlado.
    def setUp(self):
         #Ubicacion del navegar web chrome-win64
        chromium_path=r'C:\Users\HugodeJesúsMeloRange\Documents\proyectos\tarifasCFE\chrome-win64\chrome.exe'
        #Se crea una instancia de la clase Options de Selenium, que se utiliza para configurar opciones específicas para el controlador del navegador.
        options= Options()
        # representa la ubicación del archivo ejecutable del navegador Chromium
        options.binary_location=chromium_path
        options.add_argument("--disable-web-security")
        #solucionar problemas de rendimiento o incompatibilidades en la automatización del navegador.
        #options.add_argument('--disable-dev-shm-usage')
        #Ejecuta el navegador sin un sandbox, esto se relaciona con la seguridad y puede ser necesario en ciertos entornos.
        options.add_argument("--no-sandbox")
        #Ejecuta el navegador en modo sin cabeza, lo que significa que el navegador no se mostrará en la pantalla y funcionará en segundo plano.
        #Ejecuta el navegador en modo sin cabeza, lo que significa que el navegador no se mostrará en la pantalla y funcionará en segundo plano.
        options.add_argument("--headless")
        #se crea una instancia del controlador del navegador Chrome utilizando las opciones configuradas. Esta instancia de webdriver se asigna al atributo self.driver, 
        #lo que significa que estará disponible en todos los métodos de prueba dentro de la clase.
        self.driver = webdriver.Chrome(options)
    #El @mide_tiempo es un decorador que se aplica al método test_usando_select. Esto indica que el tiempo de ejecución de este método se medirá automáticamente utilizando el decorador mide_tiempo que has definido anteriormente.
    @mide_tiempo 
    def test_usando_select(self): 
        mesSistema = str(datetime.datetime.today().month)
        añoSistema = str(datetime.datetime.today().year)
        nombre_archivo = filedialog.asksaveasfilename(defaultextension=".csv")
        rutaArchivo = os.path.basename(nombre_archivo)
        #Inicialización de diccionarios para almacenar los años   
        dictAño={}
        countClickAño = 0
        #Inicialización de diccionarios para almacenar los meses   
        dictMes={}
        countClickMes = 0
        #Inicialización de diccionarios para almacenar los estados   
        dictEdo={}
        countClickEdo = 0
        #Inicialización de diccionarios para almacenar los municipios   
        dictMun={}
        countClickMun = 0
        #Inicialización de diccionarios para almacenar las divisiones   
        dictDiv={}
        countClickDiv = 0
        #Inicialización de diccionarios para almacenar las tarifas de la Comisión Federal de Electricidad (CFE) 
        tarifas_cfe={}
        #Inicialización de lista para almacenar la información generadara   
        resultado=[]
        #  crea una variable llamada driver que hace referencia al atributo driver de la clase actual.
        driver=self.driver
        # crea una variable llamada driver que hace referencia al atributo driver de la clase actual.
        driver.get("https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRENegocio/Tarifas/GranDemandaMTH.aspx")    
        #El método find_element devuelve el primer elemento que cumpla con el tipo de busqueda definido por el parámetro by
        selectAño=driver.find_element(By.XPATH,'/html/body/form/section/div/div[1]/div[2]/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/select')
        #Devuelve una lista con elementos encontrados que cumplan con el tipo de busqueda definida por el parametro by
        opcAño=selectAño.find_elements(By.TAG_NAME,"option")
       
        # Un bucle for para iterar a través de la variable llamada opcAño que es una lista que contiene elementos de la página web.
        #Dentro del bucle for, se crea un diccionario llamado dictAño, Cada elemento en opcAño se procesa individualmente y se agrega al 
        # diccionario dictAño como una clave-valor. La clave del diccionario se establece como el atributo value del elemento opc, 
        # que se obtiene utilizando el método get_attribute() en opc. 
        # El valor del diccionario se establece como el texto del elemento opc, que se obtiene utilizando el atributo text en opc.
        for opc in opcAño:
            dictAño[opc.get_attribute("value")]=opc.text
        #El método find_element devuelve el primer elemento que cumpla con el tipo de busqueda definido por el parámetro by
        selectEstado=driver.find_element(By.XPATH,"/html/body/form/section/div/div[1]/div[2]/table[1]/tbody/tr[8]/td/div/div/select")
        #Devuelve una lista con elementos encontrados que cumplan con el tipo de busqueda definida por el parametro by
        opcEstado=selectEstado.find_elements(By.CSS_SELECTOR,"option")
        # Un bucle for para iterar a través de la variable llamada opcEstado que es una lista que contiene elementos de la página web.
        #Dentro del bucle for, se crea un diccionario llamado dictEdo, Cada elemento en opcEstado se procesa individualmente y se agrega al 
        # diccionario dictEdo como una clave-valor. La clave del diccionario se establece como el atributo value del elemento opc, 
        # que se obtiene utilizando el método get_attribute() en opc. 
        # El valor del diccionario se establece como el texto del elemento opc, que se obtiene utilizando el atributo text en opc.
        for opc in opcEstado:
            dictEdo[opc.get_attribute("value")]=opc.text
       #El bucle for itera sobre las claves del diccionario dictAño, donde cada clave representa un año.
        for key_año in dictAño.keys():
            #Dentro del bucle, se verifica si la clave key_año es igual a "2022" si se cumple, se realiza lo siguiente
            if key_año ==añoSistema:
                #Se utiliza el método find_element de driver para encontrar un elemento en la página web utilizando el valor del xpath proporcionado como argumento.
                #Se crea un objeto selectAño de la clase Select para interactuar con el select encontrado.
                selectAño=Select(driver.find_element(By.XPATH,'/html/body/form/section/div/div[1]/div[2]/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/select'))
                #Se selecciona una opción en el select utilizando el método select_by_value y pasando key_año como argumento. Esto establecerá el valor del select en "2022".
                selectAño.select_by_value(key_año)
                if selectAño:
                    countClickAño+=1
                #Se agrega la clave con el valor key_año al diccionario tarifas_cfe.
                tarifas_cfe['AÑO']=key_año
                #El método find_element devuelve el primer elemento que cumpla con el tipo de busqueda definido por el parámetro by
                selectMes=driver.find_element(By.XPATH,'/html/body/form/section/div/div[1]/div[2]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[2]/select')
                #Devuelve una lista con elementos encontrados que cumplan con el tipo de busqueda definida por el parametro by
                opcMes=selectMes.find_elements(By.CSS_SELECTOR,"option")
        # el bucle for itera a través de la variable llamada opcMes que es una lista que contiene elementos de la página web.
        #Dentro del bucle for, se crea un diccionario llamado dictMes, Cada elemento en opcMes se procesa individualmente y se agrega al 
        # diccionario dictMes como una clave-valor. La clave del diccionario se establece como el atributo value del elemento opc, 
        # que se obtiene utilizando el método get_attribute() en opc. 
        # El valor del diccionario se establece como el texto del elemento opc, que se obtiene utilizando el atributo text en opc.
        for opc in opcMes:
            dictMes[opc.get_attribute("value")]=opc.text
        # el bucle for itera sobre los elementos del diccionario dictMes. 
        # En cada iteración, el valor de la clave se asignará a la variable key_mes y el valor correspondiente se asignará a la variable value_mes.
        for key_mes,value_mes in dictMes.items():
            #verifica dos cosas: si key_mes es diferente de "0" y si key_mes es igual a "1". 
            # Si ambas condiciones son verdaderas, se ejecutarán las siguientes instrucciones.
            if  key_mes != "0" and key_mes == mesSistema:
                #Se utiliza el método find_element de driver para encontrar un elemento en la página web utilizando el valor del xpath proporcionado como argumento.
                #Se crea un objeto selectMes de la clase Select para interactuar con el select encontrado.
                selectMes=Select(driver.find_element(By.XPATH,"/html/body/form/section/div/div[1]/div[2]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[2]/select"))
                #Se selecciona una opción en el select utilizando el método select_by_value y pasando key_mes como argumento. Esto establecerá el valor del select en "1".
                if selectMes:
                    countClickMes+=1
                
                selectMes.select_by_value(key_mes)
                #Se agrega la clave con el valor key_año al diccionario tarifas_cfe.
                tarifas_cfe['NUMERO MES']=key_mes
                #Se agrega la clave con el valor key_año al diccionario tarifas_cfe.
                tarifas_cfe['NOMBRE MES']=value_mes
        #el bucle for itera sobre los elementos del diccionario dictEdo. 
        # En cada iteración, el valor de la clave se asignará a la variable key_edo y el valor correspondiente se asignará a la variable value_edo.
        for key_edo,value_edo in dictEdo.items():
             #verifica si key_edo es diferente de "0" . 
            if key_edo != "0":
                #se inicializaun diccionario para poder ir almacenando los valores en cada iteración
                edo_cfe={}
                #Se utiliza el método find_element de driver para encontrar un elemento en la página web utilizando el valor del xpath proporcionado como argumento.
                #Se crea un objeto selectEdo de la clase Select para interactuar con el select encontrado.
                selectEdo=Select(driver.find_element(By.XPATH, "/html/body/form/section/div/div[1]/div[2]/table[1]/tbody/tr[8]/td/div/div/select")) 
                if selectEdo:
                    countClickEdo+=1
                #Se selecciona una opción en el select utilizando el método select_by_value y pasando key_edo como argumento.   
                selectEdo.select_by_value(key_edo) 
                #El método find_element devuelve el primer elemento que cumpla con el tipo de busqueda definido por el parámetro by
                selectMun=driver.find_element(By.XPATH,"/html/body/form/section/div/div[1]/div[2]/table[1]/tbody/tr[8]/td/div/div/select[2]")
                #Devuelve una lista con elementos encontrados que cumplan con el tipo de busqueda definida por el parametro by
                opcMun=selectMun.find_elements(By.CSS_SELECTOR,"option") 
                #Se agrega la clave  con el valor key_edo al diccionario tarifas_cfe.
                tarifas_cfe['NÚMERO ESTADO']=key_edo                
                #Se agrega la clave con el valor value_edo al diccionario tarifas_cfe.
                tarifas_cfe['NOMBRE ESTADO']=value_edo  
                #actualiza el diccionario edo_cfe con los elementos del diccionario tarifas_cfe. 
                # Esto significa que los elementos existentes en edo_cfe se mantienen y se agregan los elementos de tarifas_cfe.
                edo_cfe.update(tarifas_cfe)
                # Un bucle for para iterar a través de la variable llamada opcMun que es una lista que contiene elementos de la página web.
                #Dentro del bucle for, se crea un diccionario llamado dictMun, Cada elemento en opcMun se procesa individualmente y se agrega al 
                # diccionario dictMun como una clave-valor. La clave del diccionario se establece como el atributo value del elemento opc, 
                # que se obtiene utilizando el método get_attribute() en opc. 
                # El valor del diccionario se establece como el texto del elemento opc, que se obtiene utilizando el atributo text en opc.
                for opc in opcMun:
                    dictMun[opc.get_attribute("value")]=opc.text         
                 #el bucle for itera sobre los elementos del diccionario dictMun. 
                 # En cada iteración, el valor de la clave se asignará a la variable key_mun y el valor correspondiente se asignará a la variable value_mun.
                for key_mun,value_mun in dictMun.items():
                     #verifica si key_mun es diferente de "0" . 
                    if key_mun != "0":
                        #Se utiliza el método find_element de driver para encontrar un elemento en la página web utilizando el valor del xpath proporcionado como argumento.
                        #Se crea un objeto selectEdo de la clase Select para interactuar con el select encontrado.
                        selectMun=Select(driver.find_element(By.XPATH,"/html/body/form/section/div/div[1]/div[2]/table[1]/tbody/tr[8]/td/div/div/select[2]"))
                        if selectMun:
                            countClickMun+=1
                        #Se selecciona una opción en el select utilizando el método select_by_value y pasando key_mun como argumento.   
                        selectMun.select_by_value(key_mun)
                        #El método find_element devuelve el primer elemento que cumpla con el tipo de busqueda definido por el parámetro by
                        selectDiv=driver.find_element(By.XPATH,'/html/body/form/section/div/div[1]/div[2]/table[1]/tbody/tr[8]/td/div/div/select[3]')
                        #Devuelve una lista con elementos encontrados que cumplan con el tipo de busqueda definida por el parametro by
                        opcDiv=selectDiv.find_elements(By.CSS_SELECTOR,"option")
                        #Se agrega la clave con el valor key_edo al diccionario tarifas_cfe.
                        tarifas_cfe['NÚMERO MUNICIPIO']=key_mun
                        #Se agrega la clave  con el valor value_edo al diccionario tarifas_cfe.
                        tarifas_cfe['NOMBRE MUNICIPIO']=value_mun
                        #se vacia el diccionario para poder ir almacenando los nuevos valores en cada iteración.
                        dictMun={}
                        # Un bucle for para iterar a través de la variable llamada opcDiv que es una lista que contiene elementos de la página web.
                        #Dentro del bucle for, se crea un diccionario llamado dictDiv, Cada elemento en opcDiv se procesa individualmente y se agrega al 
                        # diccionario dictDiv como una clave-valor. La clave del diccionario se establece como el atributo "value" del elemento opc, 
                        # que se obtiene utilizando el método get_attribute() en opc. 
                        # El valor del diccionario se establece como el texto del elemento opc, que se obtiene utilizando el atributo text en opc.
                        for opc in opcDiv:
                            dictDiv[opc.get_attribute("value")]=opc.text
                         #El bucle for itera sobre las claves del diccionario dictDiv, donde cada clave representa una division.
                        for key_div in dictDiv.keys():
                             #verifica si key_mun es diferente de "0" . 
                            if key_div != "0":
                               #se inicializaun diccionario para poder ir almacenando los valores en cada iteración
                               sitios_cfe={}
                                #Se utiliza el método find_element de driver para encontrar un elemento en la página web utilizando el valor del xpath proporcionado como argumento.
                                #Se crea un objeto selectEdo de la clase Select para interactuar con el select encontrado.
                               selectDiv=Select(driver.find_element(By.XPATH,'/html/body/form/section/div/div[1]/div[2]/table[1]/tbody/tr[8]/td/div/div/select[3]'))
                               if selectDiv:
                                 countClickDiv+=1
                                #Se selecciona una opción en el select utilizando el método select_by_value y pasando key_mun como argumento. 
                               selectDiv.select_by_value(key_div)
                               #Se agrega la clave con el valor key_div al diccionario tarifas_cfe.
                               tarifas_cfe['NÚMERO DIVISIÓN']=key_div
                               #se vacia el diccionario para poder ir almacenando los nuevos valores en cada iteración.
                               dictDiv={}                               
                               #El método find_element devuelve el primer elemento que cumpla con el tipo de busqueda definido por el parámetro by
                               selectTable = driver.find_element(By.XPATH,value='//*[@id="content"]/div/div[1]/div[2]/table[1]/tbody/tr[8]/td/table/tbody/tr[2]/td')
                               #Devuelve una lista con elementos encontrados que cumplan con el tipo de busqueda definida por el parametro by
                               opcTabla = selectTable.find_elements(By.CSS_SELECTOR,'.table.table-bordered.table-striped')
                               #Devuelve una lista con elementos encontrados que cumplan con el tipo de busqueda definida por el parametro by
                               #encuentra y almacena todos los elementos <h3> dentro de la tabla seleccionada en la variable selectTable.
                               selectDivision =selectTable.find_elements(by=By.TAG_NAME,value='h3')
                               # el bucle for junto con la función enumerate esta recorriendo opcTabla para obtener tanto el índice como el valor de cada elemento en la lista. 
                               for i,tabla in enumerate(opcTabla):
                                   #print("----->",tabla.text)
                                    #Se esta buscando elementos tr dentro de cada elemento de opcTabla utilizando el método find_elements del objeto tabla
                                    #obteniendo algunos valores específicos
                                    contenidoTabla = tabla.find_elements(By.TAG_NAME,value='tr')
                                    #Se divide el texto en subcadenas con el metodo join
                                    nombreDivision="".join(selectDivision[i].text)
                                    nombreTarifa=(contenidoTabla[1].text).split()
                                    cargoFijo = (contenidoTabla[1].text).split()
                                    cargoVariableB  = (contenidoTabla[2].text).split()
                                    print("--------------->",cargoVariableB)
                                    cargoVariableI  = (contenidoTabla[3].text).split()
                                    cargoVariableP  = (contenidoTabla[4].text).split()
                                    cargoDistribucion= (contenidoTabla[5].text).split()
                                    cargoCapacidad=(contenidoTabla[6].text).split()
                                    #Se agrega el valor de nombreDivision al diccionario tarifas_cfe.
                                    tarifas_cfe["NOMBRE DIVISIÓN"]=nombreDivision
                                     #Se agrega el valor de la tarifa al diccionario tarifas_cfe.
                                    tarifas_cfe["TARIFA"]=nombreTarifa[0]
                                    #Se agrega el valor de cargoFijo al diccionario tarifas_cfe.
                                    tarifas_cfe["FIJO"]=cargoFijo[10]
                                    #Se agrega el valor de cargoVariableB al diccionario tarifas_cfe.
                                    tarifas_cfe["VARIABLE BASE"]=cargoVariableB[4]
                                    #Se agrega el valor de cargoVariableI al diccionario tarifas_cfe.
                                    tarifas_cfe["VARIABLE INTERMEDIA"]=cargoVariableI[4]
                                    #Se agrega el valor de cargoVariablPe al diccionario tarifas_cfe.
                                    tarifas_cfe["VARIABLE PUNTA"]=cargoVariableP[4]
                                    #Se agrega el valor de cargoDistribucio al diccionario tarifas_cfe.
                                    tarifas_cfe["DISTRIBUCIÓN"]=cargoDistribucion[3]
                                    #Se agrega el valor de cargoCapacidad al diccionario tarifas_cfe.
                                    tarifas_cfe["CAPACIDAD"]=cargoCapacidad[3]
                                    #actualiza el diccionario edo_cfe con los elementos del diccionario tarifas_cfe. 
                                    # Esto significa que los elementos existentes en edo_cfe se mant
                                    sitios_cfe.update(tarifas_cfe)
                                    #se agrega el diccionario sitios_cfe a la lista resultado
                                    resultado.append(sitios_cfe)
                                    #se vacia el diccionario para alamacenar nuevos valores
                                    sitios_cfe={}
                    #print(resultado)    
       # abre un archivo CSV en modo de apertura ('a') en la ruta especificada.        
        with open(rutaArchivo, 'a', newline='') as f:
            # crea un objeto writer de la clase "DictWriter" que se utiliza para escribir filas en un archivo CSV a partir de diccionarios
            # se utilizan los nombres de las columnas del primer elemento de la lista "resultado" como los nombres de campo para el objeto "writer".
            writer = csv.DictWriter(f,fieldnames=resultado[0].keys())
            # se escribe el encabezado en el archivo CSV utilizando el método writeheader() del objeto writer           
            writer.writeheader()
            # se recorre la lista resultado y por cada elemento en la lista se escribe una fila en el archivo CSV utilizando el método "writerow()" del objeto "writer".
            for f in resultado:
                writer.writerow(f)
        print("Click Año",countClickAño)        
        print("Click Mes",countClickMes)        
        print("Click Estado",countClickEdo)        
        print("Click Municipio",countClickMun)        
        print("Click Division",countClickDiv)        
    # se utiliza para cerrar el navegador web que se esté utilizando en las pruebas de automatización.
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()        
