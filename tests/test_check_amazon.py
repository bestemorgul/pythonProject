from datetime import time

from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.wish_list_page import WishListPage
from tests.base_test import BaseTest


class TestCheckAmazon(BaseTest):
    amazon_homepage_url = "https://www.amazon.com/"
    email_text = "bstmrgl@hotmail.com"
    password_text = "Testqa123."
    search_input = "samsung"
    samsung_text = "SAMSUNG"
    second_page = "page=2"
    wish_list_text = "Wish List"
    item_text = "SAMSUNG Galaxy Buds Pro 2 [2022] (SM-R510) - (Gray)"
    deleted_alert_text = "Deleted"

    def test_check_amazon(self):
        home_page = HomePage(self.driver)
        home_page.send_keys_captcha_text()
        self.assertEqual(self.amazon_homepage_url, self.driver.current_url, "It is not Home Page!")
        home_page.click_account_dropdown()

        login_page = LoginPage(self.driver)
        login_page.fill_email_input(self.email_text)
        login_page.click_continue()
        login_page.fill_password_input(self.password_text)
        login_page.click_sign_in()

        home_page.fill_search_box(self.search_input)
        home_page.click_search_btn()

        category_page = CategoryPage(self.driver)
        self.assertTrue(category_page.samsung_filter_text())
        category_page.second_page_click()
        self.assertIn(self.second_page, self.driver.current_url, "You are not on the second page!")
        category_page.click_third_item(3)

        product_page = ProductPage(self.driver)
        product_page.add_to_list_btn_click()
        product_page.view_list_btn_click()
        # product_page_title = product_page.get_product_text()

        wish_list_page = WishListPage(self.driver)
        # self.assertEqual(wish_list_page.product_check(), product_page_title,"Wrong item added to the wishlist!")
        wish_list_page.delete_item()
        self.assertEqual(self.deleted_alert_text, wish_list_page.get_deleted_text(), "Wishlist is not empty!")
