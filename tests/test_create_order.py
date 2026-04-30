import pytest
import requests
import allure

from data import Urls
from conftest import cancel_order


class TestCreateOrder:

    @allure.title('Проверка, создание заказа')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], [], None])
    def test_create_order_successful(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
    

        response = requests.post(f"{Urls.MAIN_URL}/api/v1/orders", json=payload)

        assert response.status_code == 201
        assert 'track' in response.json()

