from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_cant_product_in_basket(self):
        self.is_not_element_present(*BasketPageLocators.MESSAGE_BASKET)

    def check_message_that_the_cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET), \
            'No message: Your cart is empty'
