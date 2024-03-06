
import random
import os
import sys
sys.path.append(os.getcwd())
from utils.http_methods import Http_methods

""""Описание тест-кейсов"""

class ShopAPI:
    basse_url = "http://shop.bugred.ru/api/items/"

    @staticmethod
    def get_item_info(id):
        method = "get"
        body = "?id="+id
        url = ShopAPI.basse_url+method+"/"+body
        result = Http_methods.get(url)
        print(result.json())
        return result

    @staticmethod
    def crete_new_item(type):
        method = "create"
        url = ShopAPI.basse_url + method + "/"
        if type == "full":
            body = {
                "name": "НОСОЧКИ",
                "section": "Платья",
                "description": "Модное платье",
                "size": "44",
                "color": "GREEN",
                "price": 666,
                "params": "dress"
            }
        elif type == "short":
            body = {
                "name": "Шортики",
                "section": "Платья",
                "description": "Модное платье из новой коллекции!"
            }
        result = Http_methods.post(url, body)
        res = result.json()['result']
        print(res)
        return result

    @staticmethod
    def crete_new_item_short_err(key):
        method = "create"
        url = ShopAPI.basse_url+method+"/"
        if key == "name":
            body = {
                "section": "Платья",
                "description": "Модное платье из новой коллекции!"
            }
        elif key == "section":
            body = {
                "name": "Шортики",
                "description": "Модное платье из новой коллекции!"
            }
        elif key == "description":
            body = {
                "name": "Шортики",
                "section": "Платья"
            }

        result = Http_methods.post(url, body)
        print(result.json())
        return result


    @staticmethod
    def update_item_correct(id):
        method = "update"
        url = ShopAPI.basse_url + method + "/"
        price = random.randint(100, 9000)
        body = {
            "id": f"{id}",
            "name": "НОСОЧКИ",
            "section": "Платья",
            "description": "Модное платье",
            "size": "44",
            "color": "GREEN",
            "price": price,
            "params": "dress"
        }
        result = Http_methods.put(url, body)
        print(result.json())
        return [result, price] #Возвращает 2 значения - Ответ и цену. Для того чтобы проверить правильность измений

    @staticmethod
    def update_item_incorrectId(id):
        method = "update"
        url = ShopAPI.basse_url + method + "/"
        price = random.randint(100, 9000)
        body = {
            "id": f"{id}",
            "name": "НОСОЧКИ",
            "section": "Платья",
            "description": "Модное платье",
            "size": "44",
            "color": "GREEN",
            "price": price,
            "params": "dress"
        }
        result = Http_methods.put(url, body)
        print(result.json())
        return result

    @staticmethod
    def delete_item(id):
        method = "delete"
        url = ShopAPI.basse_url + method + "/"
        price = random.randint(100, 9000)
        body = {
            "id": f"{id}"
        }
        result = Http_methods.delete(url, body)
        print(result.json())
        return result



