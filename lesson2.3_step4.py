#Задача с окном подтверждения

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #нажимаем на кнопку
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

    #работа со всплывающим окном
    confirm = browser.switch_to.alert
    confirm.accept()

    #считываем значение для переменной x 
    x_element = browser.find_element(By.ID, "input_value").text
    y = calc(x_element)

    #вводим ответ в текстовое поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    #отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
    
    
