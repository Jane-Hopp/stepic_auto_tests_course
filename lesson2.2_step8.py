#Задание на загрузку файлов
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html" 
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Jane")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Hopper")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Какая еще почта?")

    #Отправка файла
    current_dir = os.path.abspath(os.path.dirname('lesson2.2_step8.py')) #получаем путь, где лежит скрипт, то есть этот файл
    file_path = os.path.join(current_dir, 'file_m.txt') #получаем путь к файлу, который будем загружать
    file_send = browser.find_element(By.ID, "file")
    file_send.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

