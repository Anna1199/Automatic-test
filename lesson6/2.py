from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service = ChromService(ChromeDriverManager().install()))
driver.implicitly_wait(17)
driver.get("http://uitestingplayground.com/textinput")
element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(button)
driver.quit()