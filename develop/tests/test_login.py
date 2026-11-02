from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import BASE_URL
import locators as loc
import data

class TestLogin:

    def test_login_success(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*loc.LOGIN_REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.EMAIL_INPUT))

        driver.find_element(*loc.EMAIL_INPUT).send_keys(data.EXISTING_USER_EMAIL)
        driver.find_element(*loc.PASSWORD_INPUT).send_keys(data.EXISTING_USER_PASSWORD)
        driver.find_element(*loc.LOGIN_BUTTON).click()

        # Ждем появления аватара (он надежнее, чем имя)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.USER_AVATAR))
        assert driver.find_element(*loc.USER_NAME).is_displayed()
        assert driver.find_element(*loc.USER_AVATAR).is_displayed()