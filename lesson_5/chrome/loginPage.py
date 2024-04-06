from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/login')
field1 = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
field1.send_keys('tomsmith')
field2 = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
field2.send_keys('SuperSecretPassword!')
logbutton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
logbutton.click()
sleep(1)
