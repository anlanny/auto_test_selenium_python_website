from selenium.webdriver.common.by import By


class BasketPageLocators:
    MESSAGE_BASKET = (By.CSS_SELECTOR, '#content_inner > p')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    INSERT_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    INSERT_PASSWORD_1 = (By.CSS_SELECTOR, '#id_registration-password1')
    INSERT_PASSWORD_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_REG = (By.CSS_SELECTOR, '#register_form button')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.price_color')
    CHECKING_NAME_PRODUCT = (By.CSS_SELECTOR, '.alert:nth-child(1) .alertinner strong')
    CHECKING_PRICE_PRODUCT = (By.CSS_SELECTOR, '.alert:nth-child(3) .alertinner p:nth-child(1) strong')
    SUCCESS_MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, '.alert:nth-child(1)')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini .btn-default:nth-child(1)')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
