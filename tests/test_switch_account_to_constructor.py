from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials


class TestAccountToConstructorNavigation:

     def test_go_to_constructor_from_personal_cabinet(self, driver):

          driver.find_element(*Locators.ACCOUNT_BUTTON).click()
          driver.find_element(*Locators.EMAIL_INPUT).send_keys(*Credentials.email)
          driver.find_element(*Locators.PASSWORD_INPUT).send_keys(*Credentials.password)
          driver.find_element(*Locators.SUBMIT_BUTTON).click()
          driver.find_element(*Locators.ACCOUNT_BUTTON).click()
          WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
          driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
          text = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.HEADING)).text

          assert text == 'Соберите бургер'

class TestStellarBurgersLogoRedirect:

     def test_click_logo_redirects_to_constructor(self, driver):

          driver.find_element(*Locators.ACCOUNT_BUTTON).click()
          driver.find_element(*Locators.EMAIL_INPUT).send_keys(*Credentials.email)
          driver.find_element(*Locators.PASSWORD_INPUT).send_keys(*Credentials.password)
          driver.find_element(*Locators.SUBMIT_BUTTON).click()
          driver.find_element(*Locators.ACCOUNT_BUTTON).click()
          WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.STELLAR_BURGERS))
          driver.find_element(*Locators.STELLAR_BURGERS).click()
          text = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.HEADING)).text

          assert text == 'Соберите бургер'
