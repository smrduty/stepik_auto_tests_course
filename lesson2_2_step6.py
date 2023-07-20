from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "https://SunInJuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)
	x = (browser.find_element(By.ID, "input_value")).text
	y = calc(x)
	input = browser.find_element(By.ID, "answer")
	button = browser.find_element(By.TAG_NAME, "button")
	#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	#button.click()
	input.send_keys(y)
	browser.execute_script("window.scrollBy(0, 110);")
	check = browser.find_element(By.ID, "robotCheckbox")
	#browser.execute_script("return arguments[0].scrollIntoView(true);", check)
	check.click()
	radio = browser.find_element(By.ID, "robotsRule")
	#browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
	radio.click()
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()
finally:
	time.sleep(10)
	browser.quit()


	