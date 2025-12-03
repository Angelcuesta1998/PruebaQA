from selenium.webdriver.common.by import By
from utils.config import url

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(url)
    
    buttonCerrar = (By.XPATH, "//*[@id='myModal']/div/span")

    def click_button_cerrar(self):
        self.driver.find_element(*self.buttonCerrar).click()
