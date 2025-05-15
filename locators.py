from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")   # Кнопка 'Войти в аккаунт'
    NAME_INPUT = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")       # Поле ввода Имя
    EMAIL_INPUT = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")    # Поле ввода Email
    PASSWORD_INPUT = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input")# Поле ввода пароля
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")                       # Кнопка 'Войти'
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")    # Кнопка 'Оформить заказ'
    REGISTER_LINK = (By.XPATH,"//a[text()='Зарегистрироваться']")                # Ссылка 'Зарегистрироваться'
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")# Кнопка 'Зарегистрироваться'
    ERROR_INPUT = (By.XPATH,"//p[text()='Некорректный пароль']")                 # Ошибка 'Некорректный пароль'
    ACCOUNT_BUTTON = (By.XPATH,"//p[text()='Личный Кабинет']")                   # Кнопка 'Личный кабинет'
    LOGIN_LINK = (By.XPATH,"//a[text()='Войти']")                                # Ссылка 'Войти'
    RESTORE_LINK = (By.XPATH,"//a[text()='Восстановить пароль']")                # Ссылка 'Восстановить пароль'
    LOGIN_INPUT = (By.XPATH, "//input[@value='nata']")                           # Поле с заполненным именем
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")                 # Кнопка 'Конструктор'
    HEADING = (By.XPATH, "//h1[text()='Соберите бургер']")                       # Заголовок 'Соберите бургер'
    STELLAR_BURGERS = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")# Логотип STELLAR_BURGERS
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")                         # Кнопка 'Выход'
    FILLING_SECTION = (By.XPATH, "//span[text()='Начинки']")                     # Раздел 'Начинки'
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")                        # Раздел 'Соусы'
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")                          # Раздел 'Булки'
    FILLING_HEADER = (By.XPATH, "//h2[text()='Начинки']")                        # Заголовок 'Начинки'
    SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")                           # Заголовок 'Соусы'
    BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")                             # Заголовок 'Булки'