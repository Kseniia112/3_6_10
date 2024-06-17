from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_is_present(browser):
    browser.get(link)
    # time.sleep(30)

    assert browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"), "Кнопки добавления в корзину нет на странице!"