from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

input_y = browser.find_element(By.CSS_SELECTOR, "#answer")
input_y.send_keys(str(y))

button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

time.sleep(5)
browser.quit()

# не забываем оставить пустую строку в конце файла
