from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import generate_registration_data
from helper import generate_registration_data_without_a_dot_in_an_email
from helper import generate_registration_data_with_invalid_email_missing_at
from helper import generate_registration_data_with_an_invalid_password
from locators import Locators


class TestRegistrationWithNewData:

    def test_success_registration(self, driver):

        name, email, password = generate_registration_data()
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.SUBMIT_BUTTON))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()

        text = WebDriverWait(driver, 15).until(EC.visibility_of_element_located
                                              (Locators.ORDER_BUTTON)).text
        assert text == 'Оформить заказ'

    def test_cannot_register_with_empty_name(self,driver):

        name, email, password = generate_registration_data()
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()


        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    def test_cannot_register_with_an_email_without_a_dot(self,driver):

        name, invalid_email, password = generate_registration_data_without_a_dot_in_an_email()
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(invalid_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    def test_cannot_register_with_an_invalid_email_missing_at(self,driver):

        name, invalid_email, password = generate_registration_data_with_invalid_email_missing_at()
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(invalid_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    def test_cannot_register_with_an_invalid_password(self, driver):


        name, email, password = generate_registration_data_with_an_invalid_password()
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        actual_text = driver.find_element(*Locators.ERROR_INPUT).text
        assert actual_text == "Некорректный пароль"

    def test_cannot_register_with_empty_password(self, driver):

        name, email, password = generate_registration_data()
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'