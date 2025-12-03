from selenium.webdriver.common.by import By
from utils.config import url
from selenium.webdriver.common.by import By
from utils import config
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class formContacto:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    buttonCerrar = (By.XPATH, "//*[@id='myModal']/div/span")
    btnTeLlamamos = (By.XPATH, "//a[@title='Te llamamos']")
    checkBoxDP = (By.NAME,"wpforms[fields][4][]")
    mensajeExito = (By.XPATH, "//h1[@class='vc_custom_heading']") 

    #Formulario
    textNombres = (By.NAME, "wpforms[fields][1]")
    textCedula = (By.NAME, "wpforms[fields][5]")
    textTelf = (By.NAME, "wpforms[fields][2]")
    textCorreo =(By.NAME, "wpforms[fields][3]")
    btnSubmit = (By.NAME, "wpforms[submit]")


    def clickButtonT(self):
        self.driver.find_element(*self.btnTeLlamamos).click()

    def click_button_cerrar(self):
        self.driver.find_element(*self.buttonCerrar).click()

    def Formulario(self, nombres, cedula,  telefono, correo):
        self.driver.find_element(*self.textNombres).send_keys(nombres)
        self.driver.find_element(*self.textCedula).send_keys(cedula)
        self.driver.find_element(*self.textTelf).send_keys(telefono)
        self.driver.find_element(*self.textCorreo).send_keys(correo)

    def clickCheck(self):
        self.driver.find_element(*self.checkBoxDP).click()  

    def clickSubmit(self):
        self.driver.find_element(*self.btnSubmit).click()

    def ValidarMensaje(self):
        return self.wait.until(EC.visibility_of_element_located(self.mensajeExito)).text
    