from selenium import webdriver
import time
from pages.formContacto_page import formContacto
from utils import config

def abrir_navegador():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config.url)
    return driver


def test_formContacto():
   driver = abrir_navegador()          

   formularioPag = formContacto(driver)
   formularioPag.click_button_cerrar()
   time.sleep(3)
   formularioPag.clickButtonT()

   formularioPag.Formulario(config.nombre, config.cedula, config.telefono, config.correo)
   driver.execute_script("window.scrollBy(0, 250);"); time.sleep(3)
   formularioPag.clickCheck(); 
   time.sleep(3)

   formularioPag.clickSubmit()

   mensaje = formularioPag.ValidarMensaje()
   assert mensaje == "¡Gracias por contactarnos!"
   
   time.sleep(2)
   driver.quit()





  