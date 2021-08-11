import pytest
import requests
import logging


pytestmark = pytest.mark.test_leader
DATA = {"first_name": "Janet"}


def test_reqres_in():
    responce = requests.get("https://reqres.in/api/users/2")
    assert responce.status_code == 200, logging.error(f"Status code is {responce.status_code}")
    assert DATA['first_name'] == responce.json()['data']['first_name'], logging.warning(responce.json())
