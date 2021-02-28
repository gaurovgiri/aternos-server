from os import wait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Firefox
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Chrome


options = Options()
options.headless = True

# driver = Chrome(options=options,executable_path='C:\chromedriver.exe') # Chrome
driver = Firefox(options=options)

class aternos:
    

    def __init__(self):
        driver.get('https://aternos.org/go/')
        user = driver.find_element_by_css_selector('#user')
        password = driver.find_element_by_css_selector('#password')
        user.send_keys('Username')
        password.send_keys('Password')
        login = driver.find_element_by_id('login')
        login.click()
    
    def server1(self):
        s1 = driver.find_element_by_css_selector('.server-body')
        s1.click()

        try:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'start')))
            start = driver.find_element_by_id('start')
            time.sleep(10)
            start.click()
            start.click()
            start.click()

            print("Starting Server!")
            WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.fa-times-circle')))
            notif = driver.find_element_by_css_selector('.fa-times-circle')
            notif.click()

            WebDriverWait(driver,3).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.server-status-label-left')))
            ca = driver.find_element_by_css_selector('.server-status-label-left')
            print("Queue Time: "+ ca.text[4:])

        except Exception:
            print('Either the server is already running or is in queue!')

        finally:
            try:
                for i in range(int(driver.find_element_by_css_selector('.server-status-label-left').text[4:6])):
                    print('Server will be online after', driver.find_element_by_css_selector('.server-status-label-left').text[4:])
                    if int(driver.find_element_by_css_selector('.server-status-label-left').text[4:6]) == 1:
                        break
                    time.sleep(60)
                
                WebDriverWait(driver=driver,timeout=int(driver.find_element_by_css_selector('.server-status-label-left').text[4:6])*60 + 60).until(EC.element_to_be_clickable((By.ID,'confirm')))

                confirm = driver.find_element_by_id('confirm')
                confirm.click()

                print("Server is loading data. Server will be online in few seconds.")

            except Exception:
                print("Server is already online!")

server = aternos()

if __name__ == '__main__':
    server
    time.sleep(10)
    server.server1()
    input()
