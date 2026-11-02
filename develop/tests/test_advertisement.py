from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from helpers import BASE_URL
import locators as loc
import data


class TestAdvertisement:

    def test_create_advertisement_unauthorized(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*loc.PLACE_AD_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(loc.AUTH_REQUIRED_MODAL))
        assert driver.find_element(*loc.AUTH_REQUIRED_MODAL).is_displayed()

    def test_create_advertisement_authorized(self, authorized_user):
        driver = authorized_user

        place_ad_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc.PLACE_AD_BUTTON))
        ActionChains(driver).move_to_element(place_ad_btn).click().perform()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc.AD_NAME_INPUT))

        driver.find_element(*loc.AD_NAME_INPUT).send_keys(data.AD_NAME)
        description_field = driver.find_element(*loc.AD_DESCRIPTION_INPUT)
        driver.execute_script("arguments[0].value = arguments[1];", description_field, data.AD_DESCRIPTION)
        driver.find_element(*loc.AD_PRICE_INPUT).send_keys(data.AD_PRICE)

        # Категория
        category_arrow = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc.AD_CATEGORY_ARROW))
        ActionChains(driver).move_to_element(category_arrow).click().perform()
        category_option = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(loc.get_dropdown_option(data.AD_CATEGORY))
        )
        ActionChains(driver).move_to_element(category_option).click().perform()

        # Город
        city_arrow = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc.AD_CITY_ARROW))
        ActionChains(driver).move_to_element(city_arrow).click().perform()
        city_option = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(loc.get_dropdown_option(data.AD_CITY))
        )
        ActionChains(driver).move_to_element(city_option).click().perform()

        # Состояние
        radio_label = driver.find_element(*loc.get_radio_wrapper(data.AD_CONDITION))
        ActionChains(driver).move_to_element(radio_label).click().perform()

        # Публикация
        publish_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(loc.PUBLISH_BUTTON))
        ActionChains(driver).move_to_element(publish_btn).click().perform()

        # Ждем, пока вернемся на главную (появится кнопка "Разместить объявление")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.PLACE_AD_BUTTON))

        # Переходим в профиль по прямому URL
        driver.get(BASE_URL + "profile")

        # Ждем заголовок страницы профиля
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.MY_ADS_HEADER))

        # Ждем, пока карточка с объявлением загрузится и станет видимой
        card_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(loc.get_ad_card_title(data.AD_NAME))
        )

        assert card_title.is_displayed()