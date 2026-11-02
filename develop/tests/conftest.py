import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import BASE_URL
import locators as loc
import data

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--no-proxy-server")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def authorized_user(driver):
    driver.get(BASE_URL)
    driver.find_element(*loc.LOGIN_REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.EMAIL_INPUT))
    driver.find_element(*loc.EMAIL_INPUT).send_keys(data.EXISTING_USER_EMAIL)
    driver.find_element(*loc.PASSWORD_INPUT).send_keys(data.EXISTING_USER_PASSWORD)
    driver.find_element(*loc.LOGIN_BUTTON).click()
    
    # Ждем именно аватар, так как он самый надежный индикатор входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.USER_AVATAR))
    return driver