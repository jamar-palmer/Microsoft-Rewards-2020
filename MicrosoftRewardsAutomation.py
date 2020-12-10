#Bing Rewards Automation

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import time

#Chrome Driver path
PATH = "C:/Users/Jamar/Documents/Python Projects/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(3)
driver.get("https://bing.com")

def sign():
    time.sleep(3)
    signIn = driver.find_element_by_id("id_s")
    signIn.click()
    time.sleep(3)
    cred = driver.find_element_by_id("i0116")
    #Enter your email here
    cred.send_keys("PLACEHOLDER.com")
    cred.send_keys(Keys.RETURN)
    time.sleep(3)
    passTo = driver.find_element_by_id("i0118")
    #Enter your password here
    passTo.send_keys("PLACEHOLDER")
    passTo.send_keys(Keys.RETURN)
    time.sleep(5)
    
sign()
time.sleep(3)
first = driver.find_element_by_id("sb_form_q")
first.send_keys("test")
first.send_keys(Keys.RETURN)

def loop():
    for x in range(0,150):
        arb = random.randint(1,300)
        value = 'i am entering ' + str(arb)
        time.sleep(random.randint(3,6))
        ping = driver.find_element_by_id("sb_form_q")
        ping.clear()
        ping.send_keys(value)
        time.sleep(random.randint(2,8))
        go = driver.find_element_by_id("sb_form_go")
        go.click()


loop()



