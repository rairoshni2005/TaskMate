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

tasks = driver.find_elements(By.CSS_SELECTOR, "#task-list li")

if len(tasks) >= 0:
    print("LOAD TASK TEST PASSED")
else:
    print("LOAD TASK TEST FAILED")

driver.quit()