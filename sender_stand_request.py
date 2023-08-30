import requests
import configuration


# Создание заказа
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # URL, части в configuration.py
                         json=body)  # тело запроса


# Поиск заказа по треку
def get_order_by_track(track):
    # Отправляем запрос с треком. Трек передаётся аргументом и преобразуется в строку
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" + str(track))
