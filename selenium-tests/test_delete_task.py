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

tasks_before = len(driver.find_elements(By.CSS_SELECTOR, "#task-list li"))

driver.find_element(By.XPATH, "//button[text()='Delete']").click()

time.sleep(2)

tasks_after = len(driver.find_elements(By.CSS_SELECTOR, "#task-list li"))

if tasks_after < tasks_before:
    print("DELETE TEST PASSED")
else:
    print("DELETE TEST FAILED")

driver.quit()