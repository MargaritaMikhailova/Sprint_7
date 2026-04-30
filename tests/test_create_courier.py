import pytest
import requests
import json
import random
import string
import allure

from API_base import UserApi
from error_message import ErrorMessage
from conftest import courier

class TestCreateCourier:

    @allure.title('Проверка, что курьера можно создать')
    def test_create_courier_successful(self, courier):
        create_resp = courier["create_response"]
        assert create_resp.status_code == 201
        assert create_resp.json()["ok"] is True


    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    def test_create_same_courier_conflict(self, courier):
        response_duplicate = UserApi.create_courier(
            login=courier["login"],
            password=courier["password"],
            first_name=courier["firstName"],
        )

        assert response_duplicate.status_code == 409
        assert response_duplicate.json()['message'] == ErrorMessage.LOGIG_ALERADY_EXIST

    @allure.title('Проверка, что если нету пароля, запрос возвращает ошибку')
    def test_create_courier_missing_password(self, courier):
        response = UserApi.create_courier(
            login=courier["login"],
            password="",
            first_name=courier["firstName"],
        )

        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessage.LOGIN_NOT_ENOUGH

    @allure.title('Проверка, что если нету логина, запрос возвращает ошибку')
    def test_create_courier_missing_login(self, courier):
        response = UserApi.create_courier(
            login="",
            password=courier["password"],
            first_name=courier["firstName"],
        )

        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessage.LOGIN_NOT_ENOUGH

    @allure.title('Проверка, что если нету пароля, запрос возвращает ошибку')
    def test_create_courier_missing_login_password(self, courier):
        response = UserApi.create_courier(
            login="",
            password="",
            first_name=courier["firstName"],
        )

        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessage.LOGIN_NOT_ENOUGH