from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def check_name_product_in_message(self, name):
        name_product_in_message = self.browser.find_element(*ProductPageLocators.CHECKING_NAME_PRODUCT).text
        assert name == name_product_in_message, 'Product name does not match.'

    def check_price_product_in_message(self, price):
        price_product_in_message = self.browser.find_element(*ProductPageLocators.CHECKING_PRICE_PRODUCT).text
        assert price == price_product_in_message, 'Price product does not match.'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADD_TO_BASKET), \
            'Success message is presented, but should not be.'

    def should_disappeared_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_ADD_TO_BASKET), \
            'Success message is not disappeared, but should has.'
