import time

import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + '@fakemail.lol', '01234lOl56789')
        page.should_be_authorised_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
        page = ProductPage(browser, link, timeout=0)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, link)
        page.open()
        name_product = browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        price_product = browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.check_name_product_in_message(name_product)
        page.check_price_product_in_message(price_product)


@pytest.mark.need_review
@pytest.mark.parametrize('links', ['0', '1', '2', '3', '4', '5', '6',
                                   pytest.param('7', marks=pytest.mark.xfail),
                                   '8', '9'])
def test_guest_can_add_product_to_basket(browser, links):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{links}'
    page = ProductPage(browser, link)
    page.open()
    name_product = browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
    price_product = browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_name_product_in_message(name_product)
    page.check_price_product_in_message(price_product)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url, 0)
    basket_page.should_cant_product_in_basket()
    basket_page.check_message_that_the_cart_is_empty()
