from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators



class TestConstructorSectionsNavigation:

    def test_switch_between_sections_filling(self, driver):

        driver.find_element(*Locators.FILLING_SECTION).click()
        text = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.FILLING_HEADER)).text
        assert text == 'Начинки'

    def test_switch_between_sections_sauces(self, driver):

        driver.find_element(*Locators.SAUCES_SECTION).click()
        text = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.SAUCES_HEADER)).text
        assert text == 'Соусы'

    def test_switch_between_sections_buns(self, driver):

        driver.find_element(*Locators.SAUCES_SECTION).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.SAUCES_HEADER))
        driver.find_element(*Locators.FILLING_SECTION).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.FILLING_HEADER))
        driver.find_element(*Locators.BUNS_SECTION).click()
        text = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.BUNS_HEADER)).text
        assert text == 'Булки'