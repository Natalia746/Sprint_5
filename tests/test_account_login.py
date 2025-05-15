from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials


class TestAccountLogin:

    def test_successful_login_via_main_page_login_button(self, driver):

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(*Credentials.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(*Credentials.password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located
                                               (Locators.ORDER_BUTTON)).text
        assert text == 'Оформить заказ'

    def test_successful_login_via_personal_account_button(self, driver):

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(*Credentials.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(*Credentials.password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located
                                               (Locators.ORDER_BUTTON)).text
        assert text == 'Оформить заказ'

    def test_checking_account_login_via_the_registration_form(self, driver):

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(*Credentials.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(*Credentials.password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located
                                               (Locators.ORDER_BUTTON)).text
        assert text == 'Оформить заказ'

    def test_login_via_password_recovery_form_auth_link(self, driver):

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.RESTORE_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(*Credentials.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(*Credentials.password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located
                                               (Locators.ORDER_BUTTON)).text
        assert text == 'Оформить заказ'