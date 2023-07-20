from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)
	image = browser.find_element(By.TAG_NAME, "img")
	image_valuex = image.get_attribute("valuex")
	#x = image_valuex.text
	y = calc(image_valuex)
	answer_field = browser.find_element(By.ID, "answer")
	answer_field.send_keys(y)
	checkbox = browser.find_element(By.ID, "robotCheckbox")
	checkbox.click()
	radio = browser.find_element(By.ID, "robotsRule")
	radio.click()
	button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
	button.click()
finally:
	time.sleep(10)
	browser.quit()

