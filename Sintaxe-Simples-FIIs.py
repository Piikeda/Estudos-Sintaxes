from selenium import webdriver
import re
import requests


from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://fiis.com.br/"

driver.get(url)

body = driver.find_element(By.TAG_NAME,'html')
resultados = body.find_element(By.CLASS_NAME,'high-lowers')
itens = resultados.find_elements(By.CLASS_NAME,'item')
for item in itens:
    valores = item.find_element(By.CLASS_NAME,'ticker-info')
    variation = item.find_element(By.CLASS_NAME,'variation-info')
    print(valores.text)
    print(variation.text)

