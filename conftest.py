import pytest

from data import OrderData
from helpers import random_string
from API_base import OrderApi, UserApi


@pytest.fixture
def order_data():
    return dict(OrderData.ORDER_DATA)


@pytest.fixture
def courier():
    login = random_string()
    password = random_string()
    first_name = random_string()

    create_resp = UserApi.create_courier(login=login, password=password, first_name=first_name)
    assert create_resp.status_code == 201, create_resp.text

    courier_data = {
        "login": login,
        "password": password,
        "firstName": first_name,
        "create_response": create_resp,
    }

    yield courier_data

    try:
        login_resp = UserApi.login_courier(login=login, password=password)
        if login_resp.status_code != 200:
            return
        courier_id = login_resp.json().get("id")
        if courier_id is None:
            return
        UserApi.delete_courier(courier_id=int(courier_id))
    except Exception:
        return
