#!/usr/bin/env python
# coding: utf-8

# Preencher Formulário

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

capabilities = webdriver.DesiredCapabilities().CHROME.copy()
capabilities['acceptInsecureCerts'] = True

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico, desired_capabilities=capabilities, options=chrome_options)

navegador = webdriver.Chrome(service=servico)

navegador.get("https://ola.oleconsignado.com.br")

navegador.find_element('xpath', '//*[@id="Senha"]').send_keys("Corban2023*")

