from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver = webdriver.Chrome(service = ChromService(ChromeDriverManager().install()))
# driver.implicitly_wait(30)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 4
    )
src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute('src')
print(src)
driver.quit()