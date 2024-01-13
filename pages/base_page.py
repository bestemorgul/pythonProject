from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from amazoncaptcha import AmazonCaptcha


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def get_url(self):
        """
     it returns the current url of the page
        """

        return self.driver.current_url

    def get_captcha(self, *locator):
        """
     it captures the numbers on the captcha and
     send the text on the input and click submit button
        """

        link = self.driver.find_element(*locator).get_attribute('src')
        captcha = AmazonCaptcha.fromlink(link)
        captcha_value = AmazonCaptcha.solve(captcha)
        self.driver.find_element(By.ID, "captchacharacters").send_keys(captcha_value)
        self.driver.find_element(By.CSS_SELECTOR, '.a-button-text[type = "submit"]').click()

    def find_element(self, *locator):
        """
     it returns the locator
        """

        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        """
     it clicks the locator
        """

        self.driver.find_element(*locator).click()

    def send_text(self, text, *locator):
        """
     it sends the text on the locator
        """

        self.driver.find_element(*locator).send_keys(text)

    def clear_text(self, *locator):
        """
     it clears the input locator
        """

        self.driver.find_element(*locator).clear()

        return self

    """

    def wait_element(self, method, message=""):
        
        return self.wait.until(EC.element_to_be_clickable(method), message)
    """

    def get_element_list(self, *element):
        """
     it returns the locators
        """

        return self.driver.find_elements(*element)

    def go_to_second_page(self, *locator):
        """
     it scrolls down on the bottom of the page and click the locator
        """

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element(*locator).click()

    """

    def scroll_down_to_element(self, *locator):
        self.actions.move_to_element(*locator).perform()
    """

    def scroll(self):
        """
     it scrolls down on the page (0,250)
        """

        self.driver.execute_script("window.scrollBy(0, 250);")
