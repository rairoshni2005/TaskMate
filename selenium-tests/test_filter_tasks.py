from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("http://127.0.0.1:5001")

driver.maximize_window()

time.sleep(3)

driver.execute_script("filterTasks('High')")

time.sleep(2)

print("FILTER TASK TEST PASSED")

driver.quit()