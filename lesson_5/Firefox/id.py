from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('http://uitestingplayground.com/dynamicid')
for _ in range(3):
    sleep(2)
    id_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    id_button.click()
