from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x,y):
  return int(x) + int(y)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    sum_xy = calc(x,y)

    print(sum_xy)

    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    print("find_el")
    select.select_by_value(str(sum_xy))

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()