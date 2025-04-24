import pytest
from selenium import webdriver

from curl import *

@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome()
    browser.get(main_site)
    yield browser
    browser.quit()




