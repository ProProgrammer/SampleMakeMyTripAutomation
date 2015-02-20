import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "http://www.makemytrip.com"

class mmtAutomation(unittest.TestCase):

    def setUp(self):
        """
        Setup class for test cases in mmtAutomation Class
        """
        # firefox_profile = webdriver.FirefoxProfile()
        self.driver = webdriver.Firefox()

    def tearDown(self):
        driver = self.driver
        driver.close()

    def test_001_load_webpage(self):
        
        driver = self.driver
        driver.get(URL)
        
        
if __name__ == "__main__":
    unittest.main()