from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("http://127.0.0.1:5001")

driver.maximize_window()

time.sleep(2)

theme_button = driver.find_element(By.ID, "theme-toggle")

theme_button.click()

time.sleep(2)

print("THEME TOGGLE TEST PASSED")

driver.quit()