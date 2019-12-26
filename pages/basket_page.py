from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_any_item_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS), "There is basket items"

    def should_be_empty_text(self):
        assert "empty" in self.text_of_the_element(*BasketPageLocators.EMPTY_MESSAGE), "There is no empty message in the page"
