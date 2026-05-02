import time
import pytest
from selenium import webdriver
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait (20)
    driver.maximize_window ()
    driver.get("https://www.saucedemo.com")

    yield driver

    time.sleep(2)
    driver.quit()