from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

option1 = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
option1.click()
confirm = browser.switch_to.alert # переходим в модальное окно
confirm.accept()
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_xpath("//input[@id='answer']")
input1.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()
   
    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()