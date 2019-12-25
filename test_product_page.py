from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    #product_page = ProductPage(browser, browser.current_url)
    page.should_be_button_add_to_basket()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_add_message()
    page.cart_cost_should_be_equal_price_of_the_product()
    page.names_of_products_should_be_equal()

# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()