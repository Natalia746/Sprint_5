from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials


class TestPersonalCabinetNavigation:

    def test_click_personal_cabinet_redirects_to_account_page(self, driver):

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(*Credentials.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(*Credentials.password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON))

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((Locators. LOGIN_INPUT))
        )

        input_value = element.get_attribute('value')

        assert input_value == 'nata'


