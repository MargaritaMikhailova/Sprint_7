# Sprint_7 - Тестирование API учебного сервиса аренды самокатов

Автотесты для API https://qa-scooter.praktikum-services.ru/docs/

## Описание проекта

Проект содержит автоматизированные тесты для проверки API сервиса аренды самокатов:
- Создание курьера
- Логин курьера
- Создание заказа
- Список заказов

## Технологии

- **Python** 3.14.2
- **Pytest** 9.0.2
- **Allure** 2.38.1
- **Requests** 2.32.5

#### Запуск всех тестов
pytest tests/ -v

#### Запуск конкретного теста
pytest tests/test_check_orders.py -v
pytest tests/test_create_courier.py -v
pytest tests/test_create_order.py -v
pytest tests/test_login_courier.py -v

#### Открытие отчёта
allure open target/allure-report
