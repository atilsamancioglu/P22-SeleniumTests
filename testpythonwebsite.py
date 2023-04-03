import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# inherit TestCase Class and create a new test class
class TestPythonWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # should always start with test_
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://pypi.org")
        self.assertIn("PyPI", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)
        assert "There were no results for" not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
