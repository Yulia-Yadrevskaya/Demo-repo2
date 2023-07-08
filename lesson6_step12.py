from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


link = "https://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
x = x_element.text
y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
y = y_element.text
sum = int(x)+int(y)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(sum))

button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
button.click()
time.sleep(5)

# закрываем браузер после всех манипуляций
browser.quit()


