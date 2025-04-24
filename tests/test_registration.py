from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from helper import generate_registration_data
from locators import Locators


class TestRegistrationWithNewData:

    def test_sucsess_registration(self, driver):

        name, email, password = generate_registration_data()
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SUBMIT_BUTTON))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()

        text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located
                                              (Locators.ORDER_BUTTON)).text
        assert text == 'Оформить заказ'

