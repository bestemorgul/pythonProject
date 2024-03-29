import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):
    base_url = "http://www.amazon.com/"

    def setUp(self):
        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("disable-extensions")
        options.add_argument("use_subprocess")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()
