from selenium import webdriver
import time
from pages.planZapping_page import planZapping
from utils import config


def abrir_navegador():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config.url)
    return driver


def test_planZapping():
    driver = abrir_navegador()  
    planZappingPag = planZapping(driver) 
    planZappingPag.click_button_cerrar(); time.sleep(3)
    planZappingPag.click_button_planZ()
    planZappingPag.click_plan(config.tipoPlan);time.sleep(3) 
