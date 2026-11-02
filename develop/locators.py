from selenium.webdriver.common.by import By

# Главная страница
LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
PLACE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")

# Форма авторизации / регистрации
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
EMAIL_INPUT = (By.NAME, "email")
PASSWORD_INPUT = (By.NAME, "password")
REPEAT_PASSWORD_INPUT = (By.NAME, "submitPassword")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Профиль пользователя
USER_AVATAR = (By.CLASS_NAME, "circleSmall")
USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

# Ошибки валидации
ERROR_MESSAGE = (By.XPATH, "//*[text()='Ошибка']")
INPUT_ERROR_CONTAINER = (By.XPATH, "//div[contains(@class, 'input_inputError')]")

# Модальное окно «Требуется авторизация»
AUTH_REQUIRED_MODAL = (By.XPATH, "//*[text()='Чтобы разместить объявление, авторизуйтесь']")

# Форма создания объявления
AD_NAME_INPUT = (By.NAME, "name")
AD_DESCRIPTION_INPUT = (By.NAME, "description")
AD_PRICE_INPUT = (By.NAME, "price")
PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")

# Кастомные дропдауны (стрелки)
AD_CATEGORY_ARROW = (By.XPATH, "//input[@name='category']/following-sibling::button")
AD_CITY_ARROW = (By.XPATH, "//input[@name='city']/following-sibling::button")

# Профиль (Мои объявления)
MY_ADS_HEADER = (By.XPATH, "//h1[text()='Мои объявления']")

# Динамические локаторы (функции)
def get_dropdown_option(text):
    return (By.XPATH, f"//button[span[text()='{text}']]")

def get_radio_wrapper(text):
    return (By.XPATH, f"//label[text()='{text}']")

def get_ad_card_title(title):
    return (By.XPATH, f"//div[contains(@class, 'card')]//h2[text()='{title}']")

# Динамические локаторы (функции)
def get_dropdown_option(text):
    return (By.XPATH, f"//button[span[text()='{text}']]")

def get_radio_wrapper(text):
    return (By.XPATH, f"//label[text()='{text}']")

def get_ad_card_title(title):
    return (By.XPATH, f"//div[contains(@class, 'card')]//h2[text()='{title}']")