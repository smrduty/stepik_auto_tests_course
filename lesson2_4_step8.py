from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	browser.get(link)
	button = browser.find_element(By.ID, "book")
	price = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
	button.click()
	
	x = browser.find_element(By.ID, "input_value")
	input = browser.find_element(By.ID, "answer")
	input.send_keys(calc(x.text))
	button2 = browser.find_element(By.ID, "solve")
	button2.click()
finally:
	time.sleep(10)
	browser.quit()


