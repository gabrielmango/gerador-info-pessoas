from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
from pprint import pprint


service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)

URL = 'https://geradornv.com.br/gerador-pessoas/'

dados_possoa = {}

driver.get(URL)
sleep(1)

driver.find_element(By.ID, 'nv-cookie-generator-people').click()

ps = driver.find_elements(By.TAG_NAME, 'p')
for chave in ps[2:28]:
    dados_possoa[chave.text] = []
    
quantidade = int(input('Quantas pessoas devo gerar? '))

for _ in range(quantidade):
    labels = driver.find_elements(By.TAG_NAME, 'label')
    combinacao = zip(ps[2:28], labels[1:])

    for key, value in combinacao:
        key_str = key.text
        value_str = value.text
        
        for chave, valor in dados_possoa.items():
            if chave == key_str:
                dados_possoa[chave].append(value_str)
                
    driver.find_element(By.ID, 'nv-new-generator-people').click()

df = pd.DataFrame(dados_possoa)
df.to_csv('pessoas.csv', index=False)

driver.quit()