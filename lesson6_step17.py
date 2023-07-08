from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.implicitly_wait(5)


WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'100')
        )
button1 = browser.find_element(By.CSS_SELECTOR, "#book")  
button1.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

input_y = browser.find_element(By.CSS_SELECTOR, "#answer")
input_y.send_keys(str(y))
time.sleep(1)
button = browser.find_element(By.CSS_SELECTOR, "#solve")
button.click()
time.sleep(10)

# закрываем браузер после всех манипуляций

browser.quit()


