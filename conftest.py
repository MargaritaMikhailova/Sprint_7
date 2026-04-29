import random
import string

import pytest
import requests

from data import Urls


def _random_string(length: int = 10) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))


def create_courier(*, login: str, password: str, first_name: str):
    payload = {"login": login, "password": password, "firstName": first_name}
    return requests.post(f"{Urls.MAIN_URL}/api/v1/courier", json=payload, timeout=30)


def login_courier(*, login: str, password: str):
    payload = {"login": login, "password": password}
    return requests.post(f"{Urls.MAIN_URL}/api/v1/courier/login", json=payload, timeout=30)


def cancel_order(*, track: int):
    return requests.put(
        f"{Urls.MAIN_URL}/api/v1/orders/cancel",
        params={"track": track},
        timeout=30,
    )


@pytest.fixture
def courier():
    login = _random_string()
    password = _random_string()
    first_name = _random_string()

    create_resp = create_courier(login=login, password=password, first_name=first_name)
    assert create_resp.status_code == 201, create_resp.text

    courier_data = {"login": login, "password": password, "firstName": first_name}
    yield courier_data

    try:
        login_resp = login_courier(login=login, password=password)
        courier_id = login_resp.json().get("id")
        if courier_id is not None:
            requests.delete(f"{Urls.MAIN_URL}/api/v1/courier/{courier_id}", timeout=30)
    except Exception:
        pass
