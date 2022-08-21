from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    
    els = browser.find_elements(By.TAG_NAME, "placeholder"):
    for element in els:
        element.send_keys("Hello")

    element = browser.find_element(By.ID,'file')

    current_dir = os.path.abspath(os.path.dirname('file.txt'))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME,"btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()