import requests

from data import Urls, EndPoint


class UserApi:
    @staticmethod
    def create_courier(*, login: str, password: str, first_name: str):
        payload = {"login": login, "password": password, "firstName": first_name}
        return requests.post(f"{Urls.MAIN_URL}{EndPoint.COURIER}", json=payload, timeout=30)

    @staticmethod
    def login_courier(*, login: str, password: str):
        payload = {"login": login, "password": password}
        return requests.post(f"{Urls.MAIN_URL}{EndPoint.COURIER_LOGIN}", json=payload, timeout=30)

    @staticmethod
    def delete_courier(*, courier_id: int):
        return requests.delete(f"{Urls.MAIN_URL}{EndPoint.COURIER}/{courier_id}", timeout=30)

class OrderApi:

    @staticmethod
    def cancel_order(*, track: int):
        return requests.put(
            f"{Urls.MAIN_URL}{EndPoint.CANCEL_ORDER}",
            params={"track": track},
            timeout=30,
        )

    @staticmethod
    def create_order(
        *,
        firstName: str,
        lastName: str,
        address: str,
        metroStation: int,
        phone,
        rentTime: int,
        deliveryDate: str,
        comment: str,
        color,
    ):
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": color,
        }
        return requests.post(f"{Urls.MAIN_URL}{EndPoint.ORDER}", json=payload, timeout=30)

    @staticmethod
    def get_order():
        return requests.get(f"{Urls.MAIN_URL}{EndPoint.ORDER}", timeout=30)

