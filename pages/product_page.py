from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add to basket is not presented"

    def add_to_cart(self):
        product_link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        product_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_add_message(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_MESSAGE), "Added to cart message is not presented"

    def names_of_products_should_be_equal(self):
        assert self.text_of_the_element(*ProductPageLocators.PRODUCT_NAME_ADDING_TO_BASKET) == self.text_of_the_element(*ProductPageLocators.PRODUCT_NAME),\
            "Product names are not the same"

    def cart_cost_should_be_equal_price_of_the_product(self):
        assert self.text_of_the_element(*ProductPageLocators.PRODUCT_PRICE) == self.text_of_the_element(*ProductPageLocators.CART_COST),\
            "Prices of products are not the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_CART_MESSAGE), "Added to cart message is presented"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_CART_MESSAGE), "Added to cart message not disappeared"