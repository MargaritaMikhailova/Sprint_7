import pytest
import requests
import json
import random
import string
import allure

from data import Urls
from conftest import login_courier


class TestLoginCourier():

    @allure.title('Проверка, что курьер может авторизоваться')
    def test_login_courier_successful(self, courier):
        login_response = login_courier(login=courier["login"], password=courier["password"])

        assert login_response.status_code == 200
        assert 'id' in login_response.json()

    @allure.title('Проверка, что для авторизации нужно передать все обязательные поля, отсутствует пароль')
    def test_login_courier_missing_password(self):
        login_payload = {"login": "some_login", "password": ""}
        response_second = requests.post(
            f"{Urls.MAIN_URL}/api/v1/courier/login",
            json=login_payload,
            timeout=30,
        )

        assert response_second.status_code == 400
        assert response_second.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка, что для авторизации нужно передать все обязательные поля, отсутствует логин')
    def test_login_courier_missing_login(self):
        password = ''.join(random.choices(string.ascii_lowercase, k=10))

        password_payload = {
            "password": password,
        }

        response_second = requests.post(
            f"{Urls.MAIN_URL}/api/v1/courier/login",
            json=password_payload,
            timeout=30,
        )
        assert response_second.status_code == 400
        assert response_second.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_check_login_courier_not_exists(self):
        payload = {"login": "nonexistent_login_12345", "password": "nonexistent_password"}
        response = requests.post(f"{Urls.MAIN_URL}/api/v1/courier/login", json=payload, timeout=10)

        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"

    @allure.title('Проверка, что система вернёт ошибку, если неправильно указать логин или пароль, неправильный логин')
    def test_check_courier_invalid_login(self, courier):
        payload = {"login": "wrong_login_12345", "password": courier["password"]}
        response = requests.post(f"{Urls.MAIN_URL}/api/v1/courier/login", json=payload, timeout=10)

        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"

    @allure.title('Проверка, что система вернёт ошибку, если неправильно указать логин или пароль, неправильный пароль')
    def test_check_courier_invalid_password(self, courier):
        payload = {"login": courier["login"], "password": "wrong_password_12345"}
        response = requests.post(f"{Urls.MAIN_URL}/api/v1/courier/login", json=payload, timeout=10)

        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"