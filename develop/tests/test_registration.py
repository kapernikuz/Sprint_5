from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import generate_email, BASE_URL
import locators as loc
import data

class TestRegistration:

    def test_registration_success(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*loc.LOGIN_REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.NO_ACCOUNT_BUTTON))
        driver.find_element(*loc.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.REPEAT_PASSWORD_INPUT))

        driver.find_element(*loc.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*loc.PASSWORD_INPUT).send_keys(data.EXISTING_USER_PASSWORD)
        driver.find_element(*loc.REPEAT_PASSWORD_INPUT).send_keys(data.EXISTING_USER_PASSWORD)
        driver.find_element(*loc.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.USER_NAME))
        assert driver.find_element(*loc.USER_NAME).is_displayed()
        assert driver.find_element(*loc.USER_AVATAR).is_displayed()

    def test_registration_invalid_email(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*loc.LOGIN_REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.NO_ACCOUNT_BUTTON))
        driver.find_element(*loc.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.REPEAT_PASSWORD_INPUT))

        driver.find_element(*loc.EMAIL_INPUT).send_keys("invalid-email")
        driver.find_element(*loc.PASSWORD_INPUT).send_keys(data.EXISTING_USER_PASSWORD)
        driver.find_element(*loc.REPEAT_PASSWORD_INPUT).send_keys(data.EXISTING_USER_PASSWORD)
        driver.find_element(*loc.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(loc.INPUT_ERROR_CONTAINER))
        error_containers = driver.find_elements(*loc.INPUT_ERROR_CONTAINER)
        assert len(error_containers) == 3
        assert driver.find_element(*loc.ERROR_MESSAGE).is_displayed()

    def test_registration_existing_user(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*loc.LOGIN_REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.NO_ACCOUNT_BUTTON))
        driver.find_element(*loc.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.REPEAT_PASSWORD_INPUT))

        driver.find_element(*loc.EMAIL_INPUT).send_keys(data.EXISTING_USER_EMAIL)
        driver.find_element(*loc.PASSWORD_INPUT).send_keys(data.EXISTING_USER_PASSWORD)
        driver.find_element(*loc.REPEAT_PASSWORD_INPUT).send_keys(data.EXISTING_USER_PASSWORD)
        driver.find_element(*loc.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(loc.INPUT_ERROR_CONTAINER))
        error_containers = driver.find_elements(*loc.INPUT_ERROR_CONTAINER)
        assert len(error_containers) == 3
        assert driver.find_element(*loc.ERROR_MESSAGE).is_displayed()