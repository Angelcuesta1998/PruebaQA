from selenium.webdriver.common.by import By
from utils.config import url
from selenium.webdriver.common.by import By
from utils import config
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class planZapping():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    buttonCerrar = (By.XPATH, "//*[@id='myModal']/div/span")
    btnPlanZapping = (By.XPATH,"/html/body/div[1]/div/header/div/div/div[1]/div/div[2]/ul/li[2]/a")

    plan_basico = (By.XPATH, "//img[@src='https://www.xtrim.com.ec/wp-content/uploads/2025/06/logo_zappbasicov2.png']")
    plan_plus = (By.XPATH, "//img[@src='https://www.xtrim.com.ec/wp-content/uploads/2025/06/logo_zappplus.png']")
    plan_premium = (By.XPATH, "//img[@src='https://www.xtrim.com.ec/wp-content/uploads/2025/03/logo_zapppremium2.svg']")



    def click_button_cerrar(self):
        self.driver.find_element(*self.buttonCerrar).click()
    
    def click_button_planZ(self):
        self.driver.find_element(*self.btnPlanZapping).click()


    def click_plan(self, tipo):
        tipo = tipo.lower()  # normalizar

        # Localizadores de las imágenes de los planes
        IMAGEN_PLAN = {
            "basico": (By.XPATH, "//img[@src='https://www.xtrim.com.ec/wp-content/uploads/2025/06/logo_zappbasicov2.png']"),
            "plus": (By.XPATH, "//img[@src='https://www.xtrim.com.ec/wp-content/uploads/2025/06/logo_zappplus.png']"),
            "premium": (By.XPATH, "//img[@src='https://www.xtrim.com.ec/wp-content/uploads/2025/03/logo_zapppremium2.svg']")
        }

        # Esperar que la página cargue
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        time.sleep(3)
        
        if tipo not in IMAGEN_PLAN:
            raise ValueError(f"Tipo de plan inválido: {tipo}")
        
        self.driver.execute_script("window.scrollBy(0, 600);")

        # Buscar el cuadro de ese plan
        time.sleep(3)
        cuadro = self.wait.until(EC.visibility_of_element_located(IMAGEN_PLAN[tipo]))

        # Buscar el botón dentro del mismo cuadro (relativo al cuadro)
        boton = cuadro.find_element(By.XPATH, "(./a[contains(text(),'Contratalo Aquí')])[2]")

        # Scroll hasta el botón y click seguro
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", boton)
        time.sleep(0.5)
        actions = ActionChains(self.driver)
        actions.move_to_element(boton).click().perform()
        time.sleep(1)


























