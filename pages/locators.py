# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "name='registration-email']")
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "name='registration-password1']")
    REPEAT_PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "name='registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div > h1")
    PRODUCT_MESSAGE_NAME = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")
    # PRODUCT_MESSAGE = (By.XPATH, '// strong[text() = "The shellcoder\'s handbook"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")
    PRODUCT_MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages>div:nth-child(3)>div>p>strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '[href="/ru/basket/"]:nth-child(1)')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_IN_BASKET = (By.CLASS_NAME, "basket-title")
