import pytest
import requests
import allure

from API_base import *

class TestCheckOrder:

    @allure.title('Проверка, что в тело ответа возвращается список заказов.')
    def test_check_order_exists(self):

        response = OrderApi.get_order()

        assert response.status_code == 200
        assert response.json()