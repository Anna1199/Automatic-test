from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/classattr')
sleep(3)
for _ in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.class3.btn-primary.btn-test")
    blue_button.click()
    sleep(4)
    alert = driver.switch_to.alert
    alert.accept()