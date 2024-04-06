from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/entry_ad')
sleep(5)
close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer")
close_button.click()
sleep(2)