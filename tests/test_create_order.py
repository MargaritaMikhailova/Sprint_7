import pytest
import requests
import allure

from API_base import *
from data import *

class TestCreateOrder(OrderApi):

    @allure.title('Проверка, создание заказа')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], [], None])
    def test_create_order_successful(self, color, order_data):

        order_data["color"] = color
        response = OrderApi.create_order(**order_data)

        assert response.status_code == 201
        assert 'track' in response.json()

