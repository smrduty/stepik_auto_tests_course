from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/huge_form.html")
	elements = browser.find_elements(By.CSS_SELECTOR, "input")
	value=["Да", "Конечно", "Нет", "Отнюдь", "Естественно", "Ясен-красен", "Вовсе нет!"]
	for element in elements:
		element.send_keys(random.choice(value))

	button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()

finally:
	time.sleep(10)
	browser.quit()

