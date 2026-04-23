
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration_1():
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

      # Ваш код, который заполняет обязательные поля
        input_0 = browser.find_element(By.CLASS_NAME, "first")
        input_0.send_keys("Ололошка")

        input_1_1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second[placeholder="Input your last name"]')
        input_1_1.send_keys("Трололо")

        input_2 = browser.find_element(By.CLASS_NAME, "third")
        input_2.send_keys("psina@psina.ru")

    # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        assert welcome_text == "Congratulations! You have successfully registered!"
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #self.assertEqual ("Congratulations! You have successfully registered!", welcome_text, "Текст приветствия не совпадает!") 

        browser.quit()

def test_registration_2():

        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

      # Ваш код, который заполняет обязательные поля
        input_0 = browser.find_element(By.CLASS_NAME, "first")
        input_0.send_keys("Ололошка")

        input_1_1 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.second[placeholder="Input your last name"]')
        input_1_1.send_keys("Трололо")

        input_2 = browser.find_element(By.CLASS_NAME, "third")
        input_2.send_keys("psina@psina.ru")

    # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        assert welcome_text_elt == "Congratulations! You have successfully registered!"
        browser.quit()



