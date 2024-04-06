from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://the-internet.herokuapp.com/inputs')
field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
field.send_keys('1000')
sleep(1)
field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
field.clear()
sleep(1)
field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
field.send_keys('999')
sleep(5)