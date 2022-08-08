#Задание на прокрутку страницы вниз
#Использование js скрипта

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #считываем значение для переменной x 
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    #вводим ответ в текстовое поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    #проскроллить страницу вниз
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    #отмечаем checkbox и выбираем radiobutton
    option1 = browser.find_element(By.ID, "robotCheckbox") #
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    #отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
    
    
