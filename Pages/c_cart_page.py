from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC








class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_open_menu_hamburger (self):
        self.driver.find_element (By.ID, "react-burger-menu-btn").click()

    def click_close_menu_hamburger (self):
        close_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-burger-cross-btn"))
        )
        close_btn.click()

    def click_remove_sauce_labs_bike_light (self):
        self.driver.find_element (By.ID, "remove-sauce-labs-bike-light").click()

    def click_continue_shopping_button (self):
        self.driver.find_element (By.ID, "continue-shopping").click() 