import pytest
import requests
import json
import random
import string
import allure

from data import Urls
from conftest import _random_string, create_courier


class TestCreateCourier():

    @allure.title('Проверка, что курьера можно создать')
    def test_create_courier_successful(self):
        login = _random_string()
        password = _random_string()
        first_name = _random_string()

        response = create_courier(login=login, password=password, first_name=first_name)

        assert response.status_code == 201
        assert response.json()['ok'] is True

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    def test_create_same_courier_conflict(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["password"],
            "firstName": courier["firstName"],
        }
        response_duplicate = requests.post(f"{Urls.MAIN_URL}/api/v1/courier", json=payload, timeout=10)

        assert response_duplicate.status_code == 409
        assert response_duplicate.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка, что если нету пароля, запрос возвращает ошибку')
    def test_create_courier_missing_password(self):

        response = requests.post(f"{Urls.MAIN_URL}/api/v1/courier", json={
            "login": "testRita123",
            "firstName": "Margarita"

        })
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка, что если нету логина, запрос возвращает ошибку')
    def test_create_courier_missing_login(self):
        response = requests.post(f"{Urls.MAIN_URL}/api/v1/courier", json={
            "password": "Aa12345",
            "firstName": "Margarita"

        })
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка, что если нету пароля, запрос возвращает ошибку')
    def test_create_courier_missing_login_password(self):
        response = requests.post(f"{Urls.MAIN_URL}/api/v1/courier", json={

            "firstName": "Margarita"

        })
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"