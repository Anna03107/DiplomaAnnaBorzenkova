#Анна Борзенкова, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import scooter_requests

def create_new_order():
    track_number = scooter_requests.post_new_order()
    return track_number.json()["track"]


def test_order():
    track_number = create_new_order()
    get_response = scooter_requests.get_order(track_number)
    assert get_response.status_code == 200