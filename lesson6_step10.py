from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)
    
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "label>span+#input_value")
x = x_element.text
y = calc(x)

input_y = browser.find_element(By.CSS_SELECTOR, "#answer")
input_y.send_keys(str(y))

checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox.click()

radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
radiobutton.click()
   
button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
button.click()
time.sleep(5)

# закрываем браузер после всех манипуляций
browser.quit()


