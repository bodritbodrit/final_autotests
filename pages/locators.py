from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_for")
	REG_FORM = (By.CSS_SELECTOR, "#register_for")

class ProductPageLocators():
	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
	ADD_TO_CART_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')
	PRODUCT_NAME_ADDING_TO_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
	CART_COST = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) strong')

	
