from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Adjust if running on remote server
url = "http://localhost:5012"

driver = webdriver.Chrome()

try:
    driver.get(url)
    time.sleep(2)

    # Select a country
    select = Select(driver.find_element(By.NAME, "country"))
    select.select_by_visible_text("India")
    time.sleep(1)

    # Click the button
    driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
    time.sleep(1)

    # Check capital
    capital_text = driver.find_element(By.XPATH, "/html/body/div/h3").text
    assert "Capital of India is New Delhi" in capital_text
    print("✅ Test Passed: Capital displayed correctly")

except Exception as e:
    print("❌ Test Failed:", str(e))
    raise

finally:
    driver.quit()
