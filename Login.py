from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
import time

COOPEUCH_URL = 'https://www.google.com'

class LoginValidator:

    def __init__(self, r, p):
      self.rut = r
      self.password = p
      self.options = webdriver.ChromeOptions()
      self.options.add_argument('--ignore-certificate-errors')
      self.options.add_argument("--test-type")
      self.options.add_argument("--no-sandbox")
      self.options.add_argument("--disable-dev-shm-usage")
      self.browser = webdriver.Chrome("./chromedriver",chrome_options=self.options)
      self.browser.get(COOPEUCH_URL)
      # Browser maximize
      self.maximize()

    def maximize(self):
      self.browser.maximize_window()

    def access(self):
      try:
        search = WebDriverWait( self.browser, 5).until(EC.presence_of_element_located((By.NAME, "q")), message='Rut not found')

       # pwdBox = WebDriverWait( self.browser, 5).until(EC.presence_of_element_located((By.NAME, "password")), message='Password not found')

      #  enterButton = WebDriverWait( self.browser, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/div[1]/form/button")), message='Enter Button not found')

        enterButton = WebDriverWait( self.browser, 5).until(EC.presence_of_element_located((By.NAME, "btnK")), message='Enter Button not found')


        print('Ingresando rut : ',  self.rut)
        # search.send_keys(self.rut)
        search.send_keys("hola nelson sapin")
        # print('Ingresando contraseña : ', self.password)
        # pwdBox.send_keys( self.password)

        print('Inicio Busqueda ..')
        enterButton.submit()

      except TimeoutException as e:
        print('{}: |ERROR| TimeoutException waiting for search input field,  {}'.format( self.browser.name, e))



