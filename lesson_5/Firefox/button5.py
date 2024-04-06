from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
for _ in range(5):
    add_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    add_button.click()
    sleep(0.5)

delete_buttons = driver.find_elements(By.CSS_SELECTOR, "button[onclick='deleteElement()']")
print(f'Количество кнопок "Delete": {len(delete_buttons)}')