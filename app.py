from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())



driver = webdriver.Chrome(executable_path="/opt/render/project/.render/chrome/opt/google/chrome/google-chrome/chromedriver",
                                   desired_capabilities=capabilities,options=chrome_options)

navegador = webdriver.Chrome(service=servico)

navegador.get("https://ola.oleconsignado.com.br")

navegador.find_element('xpath', '//*[@id="Senha"]').send_keys("Corban2023*")
