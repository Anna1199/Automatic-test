from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/dynamicid')
for _ in range(3):
    sleep(2)
    id_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    id_button.click()

