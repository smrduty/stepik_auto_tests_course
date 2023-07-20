from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
	#link = "https://suninjuly.github.io/selects1.html"
	link = "https://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	number1 = browser.find_element(By.ID, "num1")
	number2 = browser.find_element(By.ID, "num2")
	sum = int(number1.text) + int(number2.text)
	selection = Select(browser.find_element(By.TAG_NAME, "select"))
	selection.select_by_visible_text(str(sum))
	button = browser.find_element(By.TAG_NAME, "button")
	button.click()
finally:
	time.sleep(10)
	browser.quit()



