import random

class Urls:
    MAIN_URL = "https://qa-scooter.praktikum-services.ru"

class OrderData:
    ORDER_DATA = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
    }

class EndPoint:
    COURIER = "/api/v1/courier"
    COURIER_LOGIN = "/api/v1/courier/login"
    CANCEL_ORDER = "/api/v1/orders/cancel"
    ORDER = "/api/v1/orders"