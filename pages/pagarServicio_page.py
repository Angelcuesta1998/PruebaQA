from selenium.webdriver.common.by import By
from utils.config import url
from selenium.webdriver.common.by import By
from utils import config
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


class pagarServicio():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


    buttonCerrar = (By.XPATH, "//*[@id='myModal']/div/span")
    btnPagarServicio = (By.XPATH,"//a[contains(@class,'mega-menu-link') and contains(@class,'fa-credit-card')]")
    #btnContinuar = (By.XPATH,"//button[.//span[text()='Continuar']]")
    textoDebito = (By.XPATH,"//span[text()='¿Tu pago es a través de débito bancario?']")

    def click_button_cerrar(self):
        self.driver.find_element(*self.buttonCerrar).click()


    def click_button_PS(self):
        element = self.wait.until(EC.element_to_be_clickable(self.btnPagarServicio))
        element.click()

    def loadingText(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.textoDebito))
            print("Texto visible:", element.text)
            return True 
        except:
            return False
        
    def ClickContinuar(self):
        try:
            if self.loadingText():
                btnContinuar = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/div/app-home/x-present-modal/div/div[2]/div/div/x-button/button"))
                )
                btnContinuar.click()
            else:
                print("El texto de débito no está presente")
        except ElementClickInterceptedException:
            print("Elemento no encontrado")
        except Exception as e:
            print(f"Ocurrió un error inesperado al intentar hacer clic en Continuar: {e}")

    
    
    def selectIdentificacion(self):
        identificacion = config.identificacion.strip()
        
        try:
            xpath_div = f"//div[contains(normalize-space(text()), '{identificacion}')]"

            elemento = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath_div))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elemento)
            elemento.click()
        except TimeoutException:
            print(f"No se encontró el elemento '{identificacion}'")
    


    def ImputIdentificacion(self):
        identificacion = config.identificacion.strip() 
        try:
            if identificacion == "Cédula":
                placeholder_text = "Ingrese su número de Cédula"
            elif identificacion == "RUC":
                placeholder_text = "Ingrese su número de RUC"
            elif identificacion == "Pasaporte":
                placeholder_text = "Ingrese su número de Pasaporte"
            else:
                return

            input_elemento = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, f"//input[@placeholder='{placeholder_text}']")
                )
            )
            input_elemento.click()
            input_elemento.clear()
            input_elemento.send_keys(config.valorIdentificacion)
            time.sleep(3)
            print(f"Se ingresó {config.valorIdentificacion} en {identificacion}")

        except Exception as e:
            print(f"Ocurrio un Error: {e}")

    
    def clickCheked(self):
        try:
            checkbox = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@type='checkbox' and contains(@class,'form-checkbox')]")
                )
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            checkbox.click()
            time.sleep(3)
        except Exception as e:
            print(f" No se pudo hacer click en el checkbox: {e}")


    def click_continuar2(self):
        try:
            # localizamos el span por su texto
            btnContinuar = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space(text())='Continuar']")
                )
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", btnContinuar)
            btnContinuar.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error': {e}")



