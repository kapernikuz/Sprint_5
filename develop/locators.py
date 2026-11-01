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

# Профиль пользователя (после авторизации)
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

# Категория и Город — кастомные дропдауны
AD_CATEGORY_INPUT = (By.NAME, "category")
AD_CITY_INPUT = (By.NAME, "city")

# Радиокнопки состояния товара
AD_CONDITION_RADIO = (By.NAME, "condition")

PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")

# Блок «Мои объявления» в профиле
MY_ADS_HEADER = (By.XPATH, "//h1[text()='Мои объявления']")
AD_CARD_TITLE = (By.XPATH, "//div[contains(@class, 'card')]//h2[text()='Тестовое объявление']")