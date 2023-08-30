import data
import sender_stand_request


# Тест на ответ 200 при попытке найти заказ по треку
def test_get_order_by_track():
    track = sender_stand_request.create_new_order(data.order_body).json()["track"]  # получаем трек
    response = sender_stand_request.get_order_by_track(track)  # вызываем функцию получения заказа по треку
    assert response.status_code == 200  # убеждаемся, что код ответа 200

# Андрей Карташов, 8-я когорта — Финальный проект. Инженер по тестированию плюс
