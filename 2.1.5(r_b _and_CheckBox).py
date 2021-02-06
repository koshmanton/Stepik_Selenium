from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #ищем значение х и считаем фенкцию
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    #вставляем значение фенкции
    field = browser.find_element_by_css_selector('#answer')
    field.send_keys(y)

    #Отмечаем checkbox
    button = browser.find_element_by_css_selector('#robotCheckbox')
    button.click()

    #Выбираем radiobutton
    button = browser.find_element_by_css_selector('#robotsRule')
    button.click()

    #Отправляем ответ
    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()