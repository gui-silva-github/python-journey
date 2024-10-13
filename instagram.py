from selenium import webdriver
import time

navegador = webdriver.Chrome()

# passo 1: entrar no site do instagram
navegador.get("https://www.instagram.com/")
time.sleep(2)

# fazer login

navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("_guii__silva")
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("descubrakkk")
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(3)

# passo 3: clicar no agora não

navegador.find_element('xpath', '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(2)

# passo 4: clicar no agora não da notificação

navegador.find_element('xpath', '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(1)

# passo 5: clicar no outro agora não

navegador.find_element('xpath', ']/button[2]').click
time.sleep(1)