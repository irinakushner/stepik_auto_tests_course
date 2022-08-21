from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME,"btn-primary")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    element = browser.find_element(By.ID,"input_value")
    el_text = element.text
    y = calc(el_text)
    print(y)
    browser.find_element(By.ID,"answer").send_keys(y)


    button = browser.find_element(By.CLASS_NAME,"btn-primary")
    button.click()

    
finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()