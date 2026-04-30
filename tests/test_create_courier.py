import pytest
import requests
import json
import random
import string
import allure

from data import Urls
from error_message import ErrorMessage


class TestCreateCourier:

    @allure.title('Проверка, что курьера можно создать')
    def test_create_courier_successful(self, courier):
        create_resp = courier["create_response"]
        assert create_resp.status_code == 201
        assert create_resp.json()["ok"] is True


    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    def test_create_same_courier_conflict(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["password"],
            "firstName": courier["firstName"],
        }
        response_duplicate = requests.post(f"{Urls.MAIN_URL}/api/v1/courier", json=payload, timeout=10)

        assert response_duplicate.status_code == 409
        assert response_duplicate.json()['message'] == ErrorMessage.LOGIG_ALERADY_EXIST

    @allure.title('Проверка, что если нету пароля, запрос возвращает ошибку')
    def test_create_courier_missing_password(self):

        response = requests.post(f"{Urls.MAIN_URL}/api/v1/courier", json={
            "login": "testRita123",
            "firstName": "Margarita"

        })
        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessage.LOGIN_NOT_ENOUGH

    @allure.title('Проверка, что если нету логина, запрос возвращает ошибку')
    def test_create_courier_missing_login(self):
        response = requests.post(f"{Urls.MAIN_URL}/api/v1/courier", json={
            "password": "Aa12345",
            "firstName": "Margarita"

        })
        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessage.LOGIN_NOT_ENOUGH

    @allure.title('Проверка, что если нету пароля, запрос возвращает ошибку')
    def test_create_courier_missing_login_password(self):
        response = requests.post(f"{Urls.MAIN_URL}/api/v1/courier", json={

            "firstName": "Margarita"

        })
        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessage.LOGIN_NOT_ENOUGH