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

time.sleep(3)

driver.find_element(By.XPATH, "//button[contains(text(),'Complete')]").click()

time.sleep(2)

completed = driver.find_element(By.CSS_SELECTOR, ".completed")

if completed:
    print("COMPLETE TASK TEST PASSED")
else:
    print("COMPLETE TASK TEST FAILED")

driver.quit()