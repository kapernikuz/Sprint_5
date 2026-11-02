from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators as loc

class TestLogout:

    def test_logout_success(self, authorized_user):
        driver = authorized_user

        logout_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc.LOGOUT_BUTTON))
        logout_btn.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.LOGIN_REGISTER_BUTTON))
        assert driver.find_element(*loc.LOGIN_REGISTER_BUTTON).is_displayed()

        assert len(driver.find_elements(*loc.USER_NAME)) == 0
        assert len(driver.find_elements(*loc.USER_AVATAR)) == 0