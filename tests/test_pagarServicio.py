from selenium import webdriver
import time
from pages.pagarServicio_page import pagarServicio
from utils import config


def abrir_navegador():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config.url)
    return driver


def test_pagarServicio():
    driver = abrir_navegador()  
    pagarServicioPag = pagarServicio(driver) 
    pagarServicioPag.click_button_cerrar(); time.sleep(3)
    pagarServicioPag.click_button_PS()
    pagarServicioPag.ClickContinuar(); time.sleep(3)
    pagarServicioPag.selectIdentificacion();time.sleep(3)
    pagarServicioPag.ImputIdentificacion()
    pagarServicioPag.clickCheked()
    pagarServicioPag.click_continuar2()
   
