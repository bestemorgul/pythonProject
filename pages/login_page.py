from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "ap_email")
    CONTINUE_BTN = (By.ID, "continue")
    PASSWORD_INPUT = (By.ID, "ap_password")
    SIGN_IN_BTN = (By.ID, "signInSubmit")

    def fill_email_input(self, email):
        """
     it sends text on the email input
        """

        self.send_text(email, *self.EMAIL_INPUT)

    def click_continue(self):
        """
     it clicks continue button
        """

        self.click_element(*self.CONTINUE_BTN)

    def fill_password_input(self, password):
        """
     it sends text on the password input
        """

        self.send_text(password, *self.PASSWORD_INPUT)

    def click_sign_in(self):
        """
     it clicks the sign in button
        """

        self.click_element(*self.SIGN_IN_BTN)

