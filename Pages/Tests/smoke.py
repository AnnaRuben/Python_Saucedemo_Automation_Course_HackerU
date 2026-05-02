import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


from selenium import webdriver
from Pages.a_login_page import LoginPage
from Pages.b_products_page import ProductPage
from Pages.c_cart_page import CartPage
import time 

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("https://www.saucedemo.com")

def run_smoke_test():

# 1. Create the objects
    login_page_obj = LoginPage(driver)
    products_page_obj = ProductPage(driver)
    cart_page_obj = CartPage(driver)

# 2. Perform the actions from those objects
    login_page_obj.login ("standard_user", "secret_sauce")

    products_page_obj.select_product ()
    products_page_obj.add_product_to_cart ()
    products_page_obj.go_to_cart ()

    cart_page_obj.click_open_menu_hamburger()
    time.sleep(2)
    cart_page_obj.click_close_menu_hamburger()
    time.sleep(2)
    cart_page_obj.click_remove_sauce_labs_bike_light()
    time.sleep(2)
    cart_page_obj.click_continue_shopping_button()
    time.sleep(2)


run_smoke_test()
driver.quit()


# $env:PYTHONPATH="."; python Pages/Tests/smoke.py

