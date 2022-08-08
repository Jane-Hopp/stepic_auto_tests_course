#Задача на меняющееся значение

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Говорим Selenium ждать (12 сек.), пока цена не уменьшится
    #x = browser.find_element(By.ID, "price").text
    WebDriverWait(browser, 12).until(
      EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()

    #считываем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value").text
    y = calc(x_element)

    #вводим ответ в текстовое поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    #отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
    
    
