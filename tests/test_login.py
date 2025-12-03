from selenium import webdriver
from pages.login_page import LoginPage
from utils import config
import time
from utils.config import Browser

def abrir_navegador():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config.url)
    return driver


def ingresar_al_sistema(driver):
    login_page = LoginPage(driver)
    login_page.click_button_cerrar()
    time.sleep(1)
    return login_page


def cerrar_navegador(driver):
    time.sleep(5)
    driver.quit()


def test_login():
    driver = abrir_navegador()
    ingresar_al_sistema(driver)
    cerrar_navegador(driver)