from conftest import new_booking
from constant import BASE_URL

class TestBookings:

    """ ---------- Happy PASSED ---------- """
    """ Проверяем рабоатет ли сревер пеперед тестом """
    def test_get_check_ping(self,auth_session, new_booking):
        check = auth_session.get(f"{BASE_URL}/ping")
        assert check.status_code == 201, "Сервер не ответил, тест окончен"

    """ CREATE """
    def test_create_booking(self, auth_session, booking_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates']['checkin'], "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates']['checkout'], "Дата выезда не совпадает"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Букинг с ID : {booking_id} не удалился"

    """ PATCH """
    def test_patch_booking(self, auth_session, booking_data, new_booking):
        booking_id = new_booking

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data = {
            "firstname" : "Surf1se"
        }

        new_bookingData = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_data)
        assert new_bookingData.status_code == 200, f"patch не отрабортал"

        new_bookingData_response = new_bookingData.json()
        assert new_bookingData_response["firstname"] == booking_data["firstname"], "Имя не обновилось"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Букинг с ID : {booking_id} не удалился"

    """ PUT """
    def test_put_booking(self, auth_session, booking_data, new_booking):
        booking_id = new_booking

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data = {
            "firstname":"hyi",
            "lastname": "pizda",
            "totalprice": 3500,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-04-05",
                "checkout": "2024-04-08"
            },
            "additionalneeds": "Breakfast"
        }

        new_bookingData = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=booking_data)
        assert new_bookingData.status_code == 200, f"put не отрабортал"

        new_bookingData_response = new_bookingData.json()
        assert new_bookingData_response["firstname"] == booking_data["firstname"], "Имя не обновилось"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Букинг с ID : {booking_id} не удалился"

        print()

    """ GET """
    def test_get_bookings(self, auth_session, booking_data, new_booking):
        get_booking = auth_session.get(f"{BASE_URL}/booking")
        assert get_booking.status_code == 200

        count_getBooking = get_booking.json()
        assert len(count_getBooking) > 0, "Get - пустой"

        """Конструкция для проверки наличия ключа в теле ответа"""
        search_key = any("bookingid" in i for i in count_getBooking)
        assert search_key == True, "Get не имеет атрибута bookingid"

    """ ---------- FAILED ---------- """
    """ Тут нету проверки от бэка на корректность заполнения (например : firstname должно быть str)"""
    def test_fail_patch(self, auth_session, booking_data, new_booking):
        booking_id = new_booking

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data = {
            "firstname": 123
        }

        new_bookingData = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_data)
        assert new_bookingData.status_code == 400, f"patch отрабортал"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Букинг с ID : {booking_id} не удалился"

    """Проверка  параметра 'lastname' на обязательность"""
    def test_fail_post (self, auth_session, booking_data):
        del booking_data["lastname"]

        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 500, "Бронь создается без указания обязательного параметра"
