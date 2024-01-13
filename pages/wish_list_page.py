from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WishListPage(BasePage):
    WISHLIST_ITEM_TITLE = (By.CSS_SELECTOR, ".a-row .a-size-small h2 .a-link-normal")
    DELETE_BTN = (By.NAME, "submit.deleteItem")
    DELETED_TEXT = (By.CSS_SELECTOR, ".a-row.a-spacing-none .a-box-inner.a-alert-container .a-alert-content")

    def product_check(self):
        """
     it returns the product title on the wishlist page
        """

        return self.find_element(*self.WISHLIST_ITEM_TITLE).get_attribute('title')

    def delete_item(self):
        """
     it clicks the delete button
        """

        self.click_element(*self.DELETE_BTN)

    def get_deleted_text(self):
        """
     it returns deleted text
        """

        return self.find_element(*self.DELETED_TEXT).text

