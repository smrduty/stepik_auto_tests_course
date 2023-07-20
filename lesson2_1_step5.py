from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
	x = x_element.text
	y = calc(x)
	input = browser.find_element(By.ID, "answer")
	input.send_keys(y)
	checkbox = browser.find_element(By.ID, "robotCheckbox")
	checkbox.click()
	radio = browser.find_element(By.ID, "robotsRule")
	radio.click()
	button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
	button.click()
finally:
	time.sleep(10)
	browser.quit()

