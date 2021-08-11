import pytest
import logging
from selenium.webdriver.common.by import By


pytestmark = pytest.mark.test_leader
# Use your personal test data credentials instead of " "
TEST_DATA = [{"url": "https://yandex.ru"},
             {"mail": " "},
             {"password": " "},
             {"phone": " "}]


def test_yandex_login(driver_setup, explicit_wait):
    driver = driver_setup
    driver.get(TEST_DATA[0]['url'])
    assert driver.find_element_by_class_name('desk-notif-card__card'), logging.error("Ошибка! Вы не на галвной.")
    driver.find_element_by_class_name('desk-notif-card__login-new-item-title').click()
    explicit_wait(By.CLASS_NAME, "passp-auth-content")
    driver.find_element_by_xpath('//*[@id="passp-field-login"]').send_keys(TEST_DATA[1]['mail'])
    driver.find_element_by_xpath('//*[@id="passp:sign-in"]').click()
    explicit_wait(By.CLASS_NAME, "Textinput-Control")
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_xpath('//*[@id="passp-field-passwd"]').send_keys(TEST_DATA[2]['password'])
    except TypeError:
        click_input = driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[2]/span').click()
        click_input.send_keys(TEST_DATA[2]['password'])
    try:
        driver.find_element_by_xpath('//*[@id="passp:sign-in"]').click()
    except TypeError:
        explicit_wait(By.CLASS_NAME, "passp-auth-content")
        driver.find_element_by_xpath('//*[@id="passp-field-phone"]').send_keys(TEST_DATA[3]['phone'])
        explicit_wait(By.CLASS_NAME, "passp-auth-content")
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div[1]/div[1]/form/div[3]/button').click()

    explicit_wait(By.CLASS_NAME, "desk-notif__wrapper")
    assert driver.find_element_by_class_name('desk-notif-card__user-name'), \
        logging.error("Ошибка! Вы не авторизировались.")
