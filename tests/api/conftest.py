from selene import browser
import pytest
import allure


@allure.title('Задаем базовый URL')
@pytest.fixture(scope='function')
def url_api():
    browser.config.base_url = 'https://petstore.swagger.io/v2/pet'
    return browser.config.base_url
