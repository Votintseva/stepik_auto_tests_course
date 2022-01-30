from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

    # Ваш код, который заполняет обязательные поля

y_element = browser.find_element_by_xpath("//span[@id='num1']").text
x_element = browser.find_element_by_xpath("//span[@id='num2']").text
print(type("x_element"))
x= x_element
y = y_element
total = (int(x)+int(y))
total = str(total)
option1 = browser.find_element_by_xpath("//select[@id='dropdown']")
option1.click()
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(total) 
button = browser.find_element_by_css_selector("button.btn")
button.click()
   
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()