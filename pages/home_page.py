from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    ACCOUNT_DROPDOWN = (By.CLASS_NAME, 'nav-line-1-container')
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    CAPTCHA_SRC = (By.XPATH, '//div[@class = "a-row a-text-center"]//img')

    amazon_homepage_url = "https://www.amazon.com/"

    def click_account_dropdown(self):
        """
     it clicks the account
        """

        self.click_element(*self.ACCOUNT_DROPDOWN)

    def send_keys_captcha_text(self):
        """
     it catches the text on the captcha and
     send the text on the input and
     clicks submit button
        """

        self.get_captcha(*self.CAPTCHA_SRC)

    def fill_search_box(self, search_input):
        """
     it sends text on searchbox
        """

        self.send_text(search_input, *self.SEARCH_BOX)

    def click_search_btn(self):
        """
     it clicks search button on searchbox
        """

        self.click_element(*self.SEARCH_BTN)
