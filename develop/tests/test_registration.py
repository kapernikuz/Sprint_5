from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import generate_email, BASE_URL
import locators as loc


def _open_registration_form(driver):
    driver.get(BASE_URL)
    driver.find_element(*loc.LOGIN_REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(loc.NO_ACCOUNT_BUTTON)
    )
    driver.find_element(*loc.NO_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(loc.REPEAT_PASSWORD_INPUT)
    )


def test_registration_success(driver):
    _open_registration_form(driver)

    driver.find_element(*loc.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*loc.PASSWORD_INPUT).send_keys("TestPass123!")
    driver.find_element(*loc.REPEAT_PASSWORD_INPUT).send_keys("TestPass123!")
    driver.find_element(*loc.CREATE_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.USER_NAME))

    assert driver.find_element(*loc.USER_NAME).is_displayed()
    assert driver.find_element(*loc.USER_AVATAR).is_displayed()


def test_registration_invalid_email(driver):
    _open_registration_form(driver)

    driver.find_element(*loc.EMAIL_INPUT).send_keys("invalid-email")
    driver.find_element(*loc.PASSWORD_INPUT).send_keys("TestPass123!")
    driver.find_element(*loc.REPEAT_PASSWORD_INPUT).send_keys("TestPass123!")
    driver.find_element(*loc.CREATE_ACCOUNT_BUTTON).click()

    # Ждём появления контейнера с ошибкой
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(loc.INPUT_ERROR_CONTAINER)
    )

    # Проверяем, что выделено 3 поля (Email, Пароль, Повтор)
    error_containers = driver.find_elements(*loc.INPUT_ERROR_CONTAINER)
    assert len(error_containers) == 3
    assert driver.find_element(*loc.ERROR_MESSAGE).is_displayed()


def test_registration_existing_user(driver):
    _open_registration_form(driver)

    driver.find_element(*loc.EMAIL_INPUT).send_keys("existing@test.ru")
    driver.find_element(*loc.PASSWORD_INPUT).send_keys("TestPass123!")
    driver.find_element(*loc.REPEAT_PASSWORD_INPUT).send_keys("TestPass123!")
    driver.find_element(*loc.CREATE_ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(loc.INPUT_ERROR_CONTAINER)
    )

    error_containers = driver.find_elements(*loc.INPUT_ERROR_CONTAINER)
    assert len(error_containers) == 3
    assert driver.find_element(*loc.ERROR_MESSAGE).is_displayed()