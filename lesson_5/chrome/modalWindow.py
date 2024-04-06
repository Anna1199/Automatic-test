from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/entry_ad')
sleep(5)
close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer")
close_button.click()
sleep(2)