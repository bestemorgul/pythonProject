import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class TestCheckLcwaikikiCart(unittest.TestCase):
    LCW_HOME = (By.CSS_SELECTOR,
                ".menu-header-item__title[href='https://www.lcwaikiki.com/tr-TR/TR/lp/lcw-home']")
    BEST_SELLING = (By.CSS_SELECTOR,
                    "img[alt='ÇOK SATANLAR']")
    FIRST_ITEM = (By.XPATH, "//img[@class='product-image__image'][1]")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR,
                       "#pd_add_to_cart")
    GO_TO_CART_BTN = (By.LINK_TEXT, "Sepete Git")

    base_url = "https://www.lcwaikiki.com/tr-TR/TR"
    lcw_home_url = "https://www.lcwaikiki.com/tr-TR/TR/lp/lcw-home"
    cart_btn_text = "Sepete Git"
    title_of_the_page = "En Çok Satan Ev Ürünleri - LC Waikiki"
    add_to_cart_btn_text = "SEPETE EKLE"
    cart_page_title = "Sepetim"
    home_page_title = "LC Waikiki"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def test_check_lcwaikiki_cart(self):
        self.driver.find_element(*self.LCW_HOME).click()
        self.assertEqual(self.lcw_home_url, self.driver.current_url)

        self.driver.find_element(*self.BEST_SELLING).click()
        self.assertTrue(self.title_of_the_page == self.driver.title)

        self.driver.find_element(*self.FIRST_ITEM).click()
        self.assertEqual(self.add_to_cart_btn_text, self.driver.find_element(*self.ADD_TO_CART_BTN).text)

        self.driver.find_element(*self.ADD_TO_CART_BTN).click()
        self.assertTrue(self.ADD_TO_CART_BTN)

        self.assertEqual(self.cart_btn_text, self.wait.until(EC.element_to_be_clickable(self.GO_TO_CART_BTN)).text)
        self.driver.find_element(*self.GO_TO_CART_BTN).click()
        self.assertIn(self.cart_page_title, self.driver.title)

        self.driver.get(self.base_url)
        self.assertIn(self.home_page_title, self.driver.title)

    def tearDown(self):
        self.driver.quit()
