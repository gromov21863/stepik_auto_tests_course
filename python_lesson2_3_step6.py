from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os
import math

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/redirect_accept.html")

try:
    knop = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    time.sleep(1)
    knop.click()
   

    all_windows = driver.window_handles
    print(f"Всего вкладок: {len(all_windows)}")
    print(f"Имена вкладок: {all_windows}")

    #confirm = driver.switch_to.alert # алерт с выбором 
    # alert = browser.switch_to.alert алерт с 
    #confirm.dismiss() ..Для отказа
    #prompt = browser.switch_to.alert  аллерт с вводом текста и согласием/отказом
    #prompt.send_keys("My answer")
    #prompt.accept()
    #confirm.accept() #для согласия

    new_window = all_windows[1]
    driver.switch_to.window(new_window)
    print("Переключились на новую вкладку")

    def calc(x):
        return str(math.log(abs(12 * math.sin(float(x)))))
    
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = driver.find_element(By.ID, "answer")
    input.send_keys(y)

    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()
