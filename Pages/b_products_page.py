from selenium.webdriver.common.by import By








class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def select_product (self):
        self.driver.find_element (By.ID, "item_0_title_link").click()

    def add_product_to_cart (self): 
        self.driver.find_element (By.ID, "add-to-cart").click()

    def go_to_cart (self):
        self.driver.find_element (By.CLASS_NAME, "shopping_cart_link").click()

              