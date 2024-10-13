from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get('https://www.netflix.com/br/login')
time.sleep(2)
navegador.find_element('xpath', '//*[@id="id_userLoginId"]').send_keys("fulano@gmail.com")
time.sleep(2)
navegador.find_element('xpath', '//*[@id="id_password"]').send_keys('senha1234')
time.sleep(2)
navegador.find_element('xpath','//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
time.sleep(2)
navegador.find_element('xpath','//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]').click()
time.sleep(2)
navegador.find_element('xpath','//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/button/svg').click()