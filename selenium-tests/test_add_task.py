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

driver.find_element(By.ID, "task-name").send_keys("Selenium Task")

driver.find_element(By.ID, "task-due").send_keys("2026-06-01T18:00")

driver.find_element(By.ID, "task-priority").send_keys("High")

driver.find_element(By.ID, "task-form").submit()

time.sleep(2)

tasks = driver.find_elements(By.CSS_SELECTOR, "#task-list li")

found = False

for task in tasks:
    if "Selenium Task" in task.text:
        found = True

if found:
    print("ADD TASK TEST PASSED")
else:
    print("ADD TASK TEST FAILED")

driver.quit()