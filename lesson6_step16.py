from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
button.click()

time.sleep(3)

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

input_y = browser.find_element(By.CSS_SELECTOR, "#answer")
input_y.send_keys(str(y))

button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

time.sleep(7)
browser.quit()

# не забываем оставить пустую строку в конце файла
