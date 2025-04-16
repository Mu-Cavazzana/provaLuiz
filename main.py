# Imports instalados individualmente

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

#Chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

#Tente acessar a url
try:
url = "https://www.hankeds.com.br/prova/login.html"
driver.get(url) #usa o ChromeDriver para acessar

time.sleep(2) #Pause por 2 segundos

def digitar_lento(elemento, texto, delay=0.25): #Variavel 'digitar_lento' com 3 caracteristicas
for letra in texto: #para cada letra no texto, enviar letra e pausar por 0,25
elemento.send_keys(letra) 
time.sleep(delay)


#variaveis de login
usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
senha = driver.find_element(By.ID, "password")
botao = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]")

digitar_lento(usuario, "admin")
time.sleep(1)
digitar_lento(senha, "admin123456")
time.sleep(1)

botao.click()
time.sleep(4)

if "destino.html" in driver.current_url: #se a url 'destino.html' estiver dentro do 'current_url' printe que o teste passou.
print(" Teste passou: redirecionado corretamente.")
else:
print(" Teste falhou: redirecionamento não ocorreu.")

time.sleep(5) #pausa de 5 segundos

except Exception as e: #excessão (catch error) caso ocorra algum erro durante o processo
print(" Erro durante o teste:", str(e))

finally: #para encerrar o programa no final
driver.quit()