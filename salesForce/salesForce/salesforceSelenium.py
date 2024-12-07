import time

# Librerias para selenium
from selenium import webdriver
from selenium.common import TimeoutException

# Librerias webDriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Se define la clase
class SalesForce:

    #Se inicia el navegador web
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.time_wait = 10
        
    # Se ingresa la url y se maximiza la pantalla
    def start_url(self, url, time_to_sleep):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options)
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(time_to_sleep)
        return self.driver

    # Espera que identifique el elemento en pantalla
    def text_by_xpath(self, xpath, text, time_to_sleep):
        try:
            element = WebDriverWait(self.driver, self.time_wait).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            element.clear()
            element.send_keys(text)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento xpath: " + xpath)
            print(ex.msg)

    def text_by_name(self, name, text, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.NAME, name)))
            element = self.driver.find_element(By.NAME, name)
            element.clear()
            element.send_keys(text)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento name: " + name)
            print(ex.msg)

    def text_by_id(self, id, text, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.ID, id)))
            element = self.driver.find_element(By.XPATH, id)
            element.clear()
            element.send_keys(text)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento xpath: " + id)
            print(ex.msg)

    def text_by_classname(self, CLASSNAME, text, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(
                EC.visibility_of_element_located((By.CLASS_NAME, CLASSNAME)))
            element = self.driver.find_element(By.XPATH, CLASSNAME)
            element.clear()
            element.send_keys(text)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento clase css : " + CLASSNAME)
            print(ex.msg)

    def select_xpath_by_text(self, text, xpath, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            element = Select(element)
            element.select_by_visible_text(text)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento clase css : " + xpath)
            print(ex.msg)

    def select_name_by_text(self, text, name, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.NAME, name)))
            element = self.driver.find_element(By.NAME, name)
            element = Select(element)
            element.select_by_visible_text(text)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento name : " + name)
            print(ex.msg)

    def select_xpath_by_index(self, xpath, index, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            element = Select(element)
            element.select_by_index(index)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento clase css : " + xpath)
            print(ex.msg)

    def select_xpath_by_value(self, value, xpath, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.XPATH, value)))
            element = self.driver.find_element(By.XPATH, xpath)
            element = Select(element)
            element.select_by_value(value)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento clase css : " + xpath)
            print(ex.msg)

    def click_btn_by_xpath(self, xpath, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            element.click()
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento xpath : " + xpath)
            print(ex.msg)

    def click_btn_by_css_selector(self, css_selector, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, css_selector)))
            element = self.driver.find_elements(By.CSS_SELECTOR, css_selector)
            element.click()
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento css : " + css_selector)
            print(ex.msg)

    def click_btn_by_name(self, name, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.NAME, name)))
            element = self.driver.find_element(By.NAME, name)
            element.click()
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento name : " + name)
            print(ex.msg)

    def validate_element(self, element_xpath, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(
                EC.visibility_of_element_located((By.XPATH, element_xpath)))
            element = self.driver.find_element(By.XPATH, element_xpath)
            time.sleep(time_to_sleep)
            return True
        except TimeoutException as ex:
            print("No se encontro elemento xpath : " + element_xpath)
            print(ex.msg)
            time.sleep(time_to_sleep)
            return False

    def scroll_into_view(self, element_xpath, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
            element = self.driver.find_element(By.XPATH, element_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView()", element)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento xpath : " + element_xpath)
            print(ex.msg)

    def scroll_into_element_by_name(self, element_name, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.NAME, element_name)))
            element = self.driver.find_element(By.NAME, element_name)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento name : " + element_name)
            print(ex.msg)

    def validate_identity_css(self, css, time_to_sleep):
        try:
            time.sleep(time_to_sleep)
            if len(self.driver.find_elements(By.CSS_SELECTOR, css)) > 0:
                return True
            else:
                time.sleep(time_to_sleep)
                return False
        except TimeoutException as ex:
            print("No se encontro elemento CSS : " + css)
            print(ex.msg)

    def send_keys_by_xpath(self, xpath, text, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.NAME, xpath)))
            element = self.driver.find_element(By.NAME, xpath)
            element.send_keys(text)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento XPATH : " + xpath)
            print(ex.msg)

    def send_keys_by_css_selector(self, css_selector, text, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
            element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
            element.send_keys(text)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento css_selector : " + css_selector)
            print(ex.msg)

    def send_text_by_name(self, name, text, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.NAME, name)))
            element = self.driver.find_element(By.NAME, name)
            element.send_keys(text)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento  : " + name)
            print(ex.msg)

    def send_keyboards_by_xpath(self, xpath, key: Keys, time_to_sleep):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            element.send_keys(key)
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("No se encontro elemento  : " + xpath)
            print(ex.msg)

    def get_text_by_xpath(self, xpath, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            time.sleep(time_to_sleep)
            return element.get_attribute('value')
        except TimeoutException as ex:
            print("No se encontro elemento xpath: " + xpath)
            print(ex.msg)

    def get_inner_text_by_xpath(self, xpath, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            time.sleep(time_to_sleep)
            return element.get_attribute('innerHTML')
        except TimeoutException as ex:
            print("No se encontro elemento xpath: " + xpath)
            print(ex.msg)

    def wait_element_by_xpath(self, xpath, time_to_sleep, time_to_wait):
        try:
            WebDriverWait(self.driver, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            time.sleep(time_to_sleep)
        except TimeoutException as ex:
            print("elemento" + xpath + " no encontrado después de : " + time_to_wait)
            print(ex.msg)

    #//iframe[contains(@height,'600px')]
    def change_iframe(self, xpath, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            time.sleep(time_to_sleep)
            iframe = self.driver.find_element(By.XPATH, xpath)
            print(iframe)
            self.driver.switch_to.frame(iframe)
        except TimeoutException as ex:
            print("Fallo al cambiar de iframe: xpath " + xpath)
            print(ex.msg)

    def change_iframe_by_id(self, id, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.ID, id)))
            time.sleep(time_to_sleep)
            iframe = self.driver.find_element(By.ID, id)
            print(iframe)
            self.driver.switch_to.frame(iframe)
        except TimeoutException as ex:
            print("Fallo al cambiar de iframe: id " + id)
            print(ex.msg)

    def change_iframe_by_id(self, id, time_to_sleep):
        try:
            WebDriverWait(self.driver, self.time_wait).until(EC.visibility_of_element_located((By.ID, id)))
            time.sleep(time_to_sleep)
            iframe = self.driver.find_element(By.ID, id)
            print(iframe)
            self.driver.switch_to.frame(iframe)
        except TimeoutException as ex:
            print("Fallo al cambiar de iframe: id " + id)
            print(ex.msg)

    def close_window(self):
        self.driver.close()
