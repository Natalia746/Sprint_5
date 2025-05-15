from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials


class TestAccountLogout:

    def test_user_can_logout_successfully(self, driver):

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(*Credentials.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(*Credentials.password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.SUBMIT_BUTTON))

        assert "login" in driver.current_url
