from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import time


class CategoryPage(BasePage):
    SECOND_PAGE = (By.CSS_SELECTOR, "a[aria-label='Go to page 2']")
    PRODUCTS = (By.XPATH, './/*[contains(@class, "a-size-medium")]')
    SAMSUNG_FILTER = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.check()

    # def check(self):
    #     self.wait_element(self.SECOND_PAGE, "No Second Page Button!")
    #     self.wait_element(self.PRODUCTS, "No products in the list!")
    #     self.wait_element(self.SAMSUNG_FILTER, "No result for Samsung filter!")

    def samsung_filter_text(self):
        """
     it returns samsung text locator
        """

        return self.find_element(*self.SAMSUNG_FILTER)

    def second_page_click(self):
        """
     it clicks the second page button at the bottom of the page
        """

        self.go_to_second_page(*self.SECOND_PAGE)

    def click_third_item(self, index=0):
        """
     it waits a bit and scrolls down on the page (0,250) and
     clicks the third item on the page
        """

        time.sleep(5)
        self.scroll()
        self.get_element_list(*self.PRODUCTS)[index].click()

    """
    def clicked_item(self, index=0):
        element = self.get_element_list(*self.PRODUCTS)[index]
        return element.text
    """
