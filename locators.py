from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BUTTON= (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]") # Кнопка 'Войти в аккаунт'
    NAME_INPUT = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input") # Поле ввода Имя
    EMAIL_INPUT = (By.XPATH, "//div[label[contains(text(),'Email')]]//input") # Поле ввода Email
    PASSWORD_INPUT = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input") # Поле ввода пароля
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка 'Войти'
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") # Кнопка 'Оформить заказ'
    REGISTER_LINK = (By.XPATH,"//a[text()='Зарегистрироваться']") # Ссылка 'Зарегистрироваться'
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")# Кнопка 'Зарегистрироваться'