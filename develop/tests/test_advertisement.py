from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

from helpers import BASE_URL
import locators as loc


def test_create_advertisement_unauthorized(driver):
    """Неавторизованный пользователь видит модальное окно с требованием авторизации."""
    driver.get(BASE_URL)
    driver.find_element(*loc.PLACE_AD_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(loc.AUTH_REQUIRED_MODAL)
    )

    assert driver.find_element(*loc.AUTH_REQUIRED_MODAL).is_displayed()


def test_create_advertisement_authorized(driver):
    """Авторизованный пользователь создаёт объявление и видит его в профиле."""
    driver.get(BASE_URL)
    driver.find_element(*loc.LOGIN_REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(loc.EMAIL_INPUT)
    )

    driver.find_element(*loc.EMAIL_INPUT).send_keys("existing@test.ru")
    driver.find_element(*loc.PASSWORD_INPUT).send_keys("TestPass123!")
    driver.find_element(*loc.LOGIN_BUTTON).click()

    # Клик с повторными попытками на случай StaleElement
    for _ in range(5):
        try:
            place_ad_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(loc.PLACE_AD_BUTTON)
            )
            place_ad_btn.click()
            break
        except StaleElementReferenceException:
            continue
    else:
        raise AssertionError("Не удалось кликнуть по кнопке 'Разместить объявление' после 5 попыток")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(loc.AD_NAME_INPUT)
    )

    driver.find_element(*loc.AD_NAME_INPUT).send_keys("Тестовое объявление")

    description_field = driver.find_element(*loc.AD_DESCRIPTION_INPUT)
    driver.execute_script("arguments[0].value = arguments[1];", description_field, "Описание для автотеста")

    driver.find_element(*loc.AD_PRICE_INPUT).send_keys("1500")

    # Категория
    category_arrow = driver.find_element(
        By.XPATH, "//input[@name='category']/following-sibling::button"
    )
    driver.execute_script("arguments[0].click();", category_arrow)
    category_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[span[text()='Книги']]"))
    )
    driver.execute_script("arguments[0].click();", category_option)

    # Город
    city_arrow = driver.find_element(
        By.XPATH, "//input[@name='city']/following-sibling::button"
    )
    driver.execute_script("arguments[0].click();", city_arrow)
    city_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[span[text()='Санкт-Петербург']]"))
    )
    driver.execute_script("arguments[0].click();", city_option)

    # Состояние товара
    radio_new = driver.find_element(
        By.XPATH, "//input[@name='condition' and @value='Новый']"
    )
    driver.execute_script("arguments[0].click();", radio_new)

    # Публикация
    driver.find_element(*loc.PUBLISH_BUTTON).click()

    # Ждём перехода на главную (кнопка "Разместить объявление" снова видна)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(loc.PLACE_AD_BUTTON)
    )

    # Переходим в профиль по прямому URL (клик по аватару не срабатывал)
    driver.get(BASE_URL + "profile")

    # Ждём появления заголовка "Мои объявления"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(loc.MY_ADS_HEADER)
    )

    # Проверяем, что созданное объявление есть в списке
    assert driver.find_element(*loc.AD_CARD_TITLE).is_displayed()