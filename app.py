from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import win32com.client as win32

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://ola.oleconsignado.com.br")

navegador.find_element('xpath', '//*[@id="Senha"]').send_keys("Corban2023*")
