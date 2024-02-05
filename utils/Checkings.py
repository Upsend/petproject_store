from requests import Response

"""Методы для проверки ответов на запросы"""

class Checkings:

    def check_status_code(response: Response, statusCode):
        if response.status_code == statusCode:
            print(f"Успешно, статус код - {response.status_code}")
        else:
            print("Провал!!!")
            print(f"ОР: статус код - {statusCode}")
            print(f"ФР: статус код - {response.status_code}")
        assert statusCode == response.status_code

    def check_keyword(response: Response, status, key, value):
        if status == True:
            r = response.json()['result']
        else:
            r = response.json()

        if r[key] == value:
            print(f"Успех!!! {key} = {value}")
        else:
            print("Провал!!!")
            print(f"ФР: {key} = {r['error']}")
            print(f"ОР: {key} = {value}")
        assert r[key] == value


