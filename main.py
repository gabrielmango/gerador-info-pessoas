from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from pprint import pprint

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)

URL = 'https://geradornv.com.br/gerador-pessoas/'

dados_possoa = {}

driver.get(URL)
sleep(1)

def gerar_pessoa(driver):

    labels = driver.find_elements(By.TAG_NAME, 'label')
    ps = driver.find_elements(By.TAG_NAME, 'p')

    combinacao = zip(ps[2:28], labels[1:])

    info_pessoa = {}

    for key, value in combinacao:
        key_str = key.text
        value_str = value.text
        info_pessoa[key_str] = value_str
        
    return info_pessoa

pessoas = []

for _ in range(100):
    driver.find_element(By.ID, 'nv-new-generator-people').click()
    pessoas.append(gerar_pessoa(driver))
    
pprint(pessoas)

driver.quit()