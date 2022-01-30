from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")
# говорим Selenium проверять в течение 12 секунд, пока цена не будет 100
option1 = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book")))
button.click()
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_xpath("//input[@id='answer']")
input1.send_keys(y)
button1 = browser.find_element_by_xpath("//button[@id='solve']")
browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
button1.click()


   
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # закрываем браузер после всех манипуляций


    # закрываем браузер после всех манипуляций

