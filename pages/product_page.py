import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.wish_list_page import WishListPage


class ProductPage(BasePage):
    ADD_TO_LIST_BTN = (By.ID, "add-to-wishlist-button-submit")
    LIST_NAME_INPUT = (By.NAME, "list-name")
    CREATE_LIST_BTN = (By.CLASS_NAME, "a-button-input a-declarative")
    VIEW_LIST_BTN = (By.XPATH, "//a[normalize-space()='View Your List']")
    PRODUCT_TITLE = (By.CLASS_NAME, "a-size-large product-title-word-break")

    def add_to_list_btn_click(self):
        """
     it waits a bit and scrolls down on the page (0,250) and
     clicks add to list button
        """

        time.sleep(3)
        self.scroll()
        self.click_element(*self.ADD_TO_LIST_BTN)

    def view_list_btn_click(self):
        """
     it clicks the view list button on the pop up
        """

        self.click_element(*self.VIEW_LIST_BTN)

        return WishListPage(self.driver)

    def get_product_text(self):
        """
     it returns the title of the product
        """

        return self.find_element(*self.PRODUCT_TITLE).text
