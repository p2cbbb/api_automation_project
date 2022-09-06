import json
from requests import Response
from utils.api import GoogleMapsApi
from utils.checking import Checking


"""Создание, изменение и удаление новой локации"""

class TestCreatePlace():

    def test_create_new_place(self):

        print("Метод POST")
        result_post: Response = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_staus_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)
        # print(list(token))

        print("Метод GET POST")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_staus_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', \
                                                'address', 'types', 'website', 'language'])

        print("Метод PUT")
        result_put: Response = GoogleMapsApi.put_new_place(place_id)
        Checking.check_staus_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])

        print("Метод GET PUT")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_staus_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', \
                                                'address', 'types', 'website', 'language'])

        print("Метод DELETE")
        result_delete: Response = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_staus_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])

        print("Метод GET DELETE")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_staus_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])

        print("Тестирование создания, изменения и удаления новой локации прошло успешно!!!")



