import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CountryCapitalTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_show_capital(self):
        self.driver.get("http://localhost:5012")
        time.sleep(2)
        self.driver.find_element(By.NAME, "country").send_keys("India")
        self.driver.find_element(By.XPATH, "//button[text()='Show Capital']").click()
        time.sleep(1)
        capital = self.driver.find_element(By.XPATH, "/html/body/h3").text
        self.assertIn("Capital: New Delhi", capital)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2))
