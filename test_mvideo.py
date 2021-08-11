import pytest
import logging
from selenium.webdriver.common.by import By


pytestmark = pytest.mark.test_leader
TEST_DATA = [{"url": "https://www.google.com/"},
             {"search_word": "купить кофемашину bork c804"},
             {"check_url": "mvideo.ru"}]


def test_google_search(driver_setup, explicit_wait):
    driver = driver_setup
    driver.get(TEST_DATA[0]['url'])
    explicit_wait(By.XPATH, '//*[@id="gb"]/div/div[2]/a')
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')\
        .send_keys(TEST_DATA[1]['search_word'])
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[1]')\
        .click()

    search_results = driver.find_elements_by_xpath('//div[@class="g"]')
    for i in search_results:
        get_result = i.find_element_by_xpath('.//div/div/div[1]/a/div/cite').text
        driver.implicitly_wait(10)
        while TEST_DATA[2]['check_url'] not in get_result:
            driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()
        else:
            logging.info(f"{TEST_DATA[2]['check_url']} is in search results")
            break
