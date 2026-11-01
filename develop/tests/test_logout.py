from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import BASE_URL
import locators as loc


def test_logout_success(driver):
    driver.get(BASE_URL)
    driver.find_element(*loc.LOGIN_REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(loc.EMAIL_INPUT)
    )

    driver.find_element(*loc.EMAIL_INPUT).send_keys("existing@test.ru")
    driver.find_element(*loc.PASSWORD_INPUT).send_keys("TestPass123!")
    driver.find_element(*loc.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.USER_NAME))

    driver.find_element(*loc.LOGOUT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(loc.LOGIN_REGISTER_BUTTON)
    )

    assert driver.find_element(*loc.LOGIN_REGISTER_BUTTON).is_displayed()

    user_elements = driver.find_elements(*loc.USER_NAME)
    avatar_elements = driver.find_elements(*loc.USER_AVATAR)
    assert len(user_elements) == 0
    assert len(avatar_elements) == 0