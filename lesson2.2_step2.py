from selenium import webdriver
import time

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

    # Ваш код, который заполняет обязательные поля
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_xpath("//input[@id='answer']")
input1.send_keys(y)
option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
option1.click()
option2 = browser.find_element_by_css_selector("[id='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2) #Проскроллить станицу вниз
option2.click()
button = browser.find_element_by_css_selector("button.btn")
button.click()

   
    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()