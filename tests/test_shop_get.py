from requests import Response
from utils.Checkings import Checkings
from utils.ShopAPI import ShopAPI

"""Запуск и проверка результатов тестов"""

class Test_item():

    def test_get_item_info(self):
        res_get = ShopAPI.get_item_info("200")
        Checkings.check_status_code(res_get, 200)
        Checkings.check_keyword(res_get, True, "name", "НОСОЧКИ")
        Checkings.check_keyword(res_get, True, "section", "Платья")
        Checkings.check_keyword(res_get, True, "description", "Модное платье")
        Checkings.check_keyword(res_get, True, "size", "44")
        Checkings.check_keyword(res_get, True, "color", "GREEN")
        Checkings.check_keyword(res_get, True, "price", 666)

    def test_get_item_info_wrong_id(self):
        res_get = ShopAPI.get_item_info("ff")
        Checkings.check_status_code(res_get, 200)
        Checkings.check_keyword(res_get, False, "status", "error")
        Checkings.check_keyword(res_get, False, "field_error", "id")
        Checkings.check_keyword(res_get, False, "error", "id_not_filled")
        Checkings.check_keyword(res_get, False, "message", "Поле ID товара заполнено не корректно")

    def test_get_item_info_empty_id(self):
        res_get = ShopAPI.get_item_info("")
        Checkings.check_status_code(res_get, 200)
        Checkings.check_keyword(res_get, False, "status", "error")
        Checkings.check_keyword(res_get, False, "field_error", "id")
        Checkings.check_keyword(res_get, False, "error", "id_not_filled")
        Checkings.check_keyword(res_get, False, "message", "Поле ID товара  не заполнено")

