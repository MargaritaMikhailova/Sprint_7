import pytest
import requests
import allure

from data import Urls


class TestCheckOrder:

    @allure.title('Проверка, что в тело ответа возвращается список заказов.')
    def test_check_order_exists(self):

        response = requests.get(f"{Urls.MAIN_URL}/api/v1/orders", timeout=10)

        assert response.status_code == 200
        assert response.json()