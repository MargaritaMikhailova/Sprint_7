import pytest
import requests
import json
import random
import string
import allure

from API_base import UserApi
from error_message import ErrorMessage
from helpers import *


class TestLoginCourier:

    @allure.title('Проверка, что курьер может авторизоваться')
    def test_login_courier_successful(self, courier):
        login_response = UserApi.login_courier(login=courier["login"], password=courier["password"])

        assert login_response.status_code == 200
        assert 'id' in login_response.json()

    @allure.title('Проверка, что для авторизации нужно передать все обязательные поля, отсутствует пароль')
    def test_login_courier_missing_password(self):
        response_second = UserApi.login_courier(login="some_login", password="")

        assert response_second.status_code == 400
        assert response_second.json()['message'] == ErrorMessage.INFORMATION_NOT_ENOUGH

    @allure.title('Проверка, что для авторизации нужно передать все обязательные поля, отсутствует логин')
    def test_login_courier_missing_login(self, courier):
        response_second = UserApi.login_courier(login="", password=courier["password"])

        assert response_second.status_code == 400
        assert response_second.json()['message'] == ErrorMessage.INFORMATION_NOT_ENOUGH

    @allure.title('Проверка, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_check_login_courier_not_exists(self):
        fake_login = random_string()
        fake_password = random_string()
        response_second = UserApi.login_courier(
            login=fake_login,
            password=fake_password)

        assert response_second.status_code == 404
        assert response_second.json()['message'] == ErrorMessage.LOGIN_NOT_EXISTS

    @allure.title('Проверка, что система вернёт ошибку, если неправильно указать логин или пароль, неправильный логин')
    def test_check_courier_invalid_login(self, courier):
        fake_login = random_string()
        response = UserApi.login_courier(
            login=fake_login,
            password=courier["password"])

        assert response.status_code == 404
        assert response.json()['message'] == ErrorMessage.LOGIN_NOT_EXISTS

    @allure.title('Проверка, что система вернёт ошибку, если неправильно указать логин или пароль, неправильный пароль')
    def test_check_courier_invalid_password(self, courier):
        fake_password = random_string()
        response = UserApi.login_courier(
            login=courier["login"],
            password=fake_password
        )

        assert response.status_code == 404
        assert response.json()['message'] == ErrorMessage.LOGIN_NOT_EXISTS