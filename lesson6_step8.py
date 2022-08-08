#Задача на поиск по XPATH
#Задача на автозаполнение регистрационной формы и ее отправка
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Jane")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Hopper")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Upsidedown")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Wonder country")
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
     
finally:
    #успеваем скопировать код за 30 секунд
    time.sleep(30)
    #закрываем браузер после всех манипуляций
    browser.quit()

     
