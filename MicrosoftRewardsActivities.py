#Microsoft Rewards Activities

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import time

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#Edge Driver path
PATH = "C:/Users/Jamar/Documents/Python Projects/msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.implicitly_wait(3)
driver.get("https://bing.com")

def sign():
    time.sleep(3)
    signIn = driver.find_element_by_id("id_s")
    signIn.click()
    time.sleep(3)
    cred = driver.find_element_by_id("i0116")
    cred.send_keys("jldddddd@gmail.com")
    cred.send_keys(Keys.RETURN)
    time.sleep(3)
    passTo = driver.find_element_by_id("i0118")
    passTo.send_keys("Jchunks12")
    time.sleep(1)
    passTo.send_keys(Keys.RETURN)
    time.sleep(5)
    
#sign()
#dropdown = driver.find_element_by_xpath("//span[@id= 'id_rc']")
time.sleep(5)
dropdown = driver.find_element_by_id("id_rc")    
dropdown.click()
time.sleep(2)
menu = driver.find_element_by_id("bepfm")
driver.switch_to.frame(menu)
time.sleep(3)

#Daily Set
daily = driver.find_elements_by_class_name("promo_cont")

#visitation task
daily[0].click()
time.sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

#poll task
daily[2].click()
time.sleep(3)
poll = driver.find_element_by_id("btoption0")
poll.click()
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

#quiz task
#This or That
daily[1].click()
time.sleep(3)
quiz = driver.find_element_by_id("rqStartQuiz")
quiz.click()
time.sleep(1)
for i in range(10):
    answer = driver.find_element_by_id("rqAnswerOption0")
    answer.click()
    time.sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])


#More activities
#moreAct = driver.find_element_by_css_selector('div.fc_dyn b_traits')
#moreAct = driver.find_elements_by_class_name("rw-accd-i")
#print(moreAct[1].text)
#moreAct[1].click()





#Searching integration saved for laat (Change driver to Edge first)    
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


#loop()



