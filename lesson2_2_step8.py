from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	input1 = browser.find_element(By.NAME, "firstname")
	input1.send_keys("Молочный")
	input2 = browser.find_element(By.NAME, "lastname")
	input2.send_keys("Антошка")
	input3 = browser.find_element(By.NAME, "email")
	input3.send_keys("point break")
	current_directory = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_directory, 'file.txt')
	element = browser.find_element(By.ID, 'file')
	element.send_keys(file_path)
	button = browser.find_element(By.TAG_NAME, "button")
	button.click()
finally:
	time.sleep(10)
	browser.quit()

