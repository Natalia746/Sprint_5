from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials


class TestAccountLogin:

    def test_successful_login_via_main_page_login_button(self, driver):

        email = Credentials()
        password = Credentials()

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        text = WebDriverWait(driver, 15).until(EC.visibility_of_element_located
                                               (Locators.ORDER_BUTTON)).text
        assert text == 'Оформить заказ'

