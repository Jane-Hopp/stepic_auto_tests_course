#Задача на переход по новой ссылке

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #нажимаем на кнопку
    browser.find_element(By.CSS_SELECTOR, "button").click()

    #переход по новой ссылке
    new_window = browser.window_handles[1] #массив имен всех вкладок
    browser.switch_to.window(new_window) #переключение на новую вкладку

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
    
    
