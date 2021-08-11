import pytest
from selenium import webdriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

PATH = 'driver/chromedriver'


@pytest.fixture()
def driver_setup():
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture()
def explicit_wait(driver_setup):
    def run(element_type, text):
        wait = WebDriverWait(driver_setup, 30)
        wait.until(expected_conditions.presence_of_element_located((element_type, text)))
    return run
