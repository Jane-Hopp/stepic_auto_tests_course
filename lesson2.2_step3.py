#задача на выбор значения из списка
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #считываем значения для подсчета их суммы  
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    x = str(int(num1) + int(num2))

    #находим значение и кликаем
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(x)

    #вводим ответ в текстовое поле
    #browser.find_element(By.ID, "dropdown").click()
    #browser.find_element(By.CSS_SELECTOR, "[value=x]").click()

    #отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
    
    
