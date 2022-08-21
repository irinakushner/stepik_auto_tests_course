from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#registration2 падает с ошибкой, при замене на registration1 тест должен быть успешным

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    firstname = browser.find_element(By.CSS_SELECTOR, ".first_block  .form-control.first")
    firstname.send_keys("Ivan")
    lastname = browser.find_element(By.CSS_SELECTOR, ".first_block  .form-control.second")
    lastname.send_keys("Ivanov")
    email = browser.find_element(By.CLASS_NAME, "form-control.third")
    email.send_keys("test@test.test")

    # Заполняем необязательные поля
    phone = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
    phone.send_keys("88005553535")
    address = browser.find_element(By.CSS_SELECTOR, ".form-group.second_class .form-control.second")
    address.send_keys("Leningrad")

    # Коммент от автора - я знаю, что можно было проще
    # Но я проходу 6 и 7 часть одним днем.Также у меня собесы
    # Я устала и просто хочу качественно выполнить задание, но без красоты в локаторах

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
