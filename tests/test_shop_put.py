from requests import Response
from utils.Checkings import Checkings
from utils.ShopAPI import ShopAPI

"""Запуск и проверка результатов тестов"""

class Test_item_update():

    def test_update_item_correct(self):
        res_put = ShopAPI.update_item_correct("176")
        Checkings.check_status_code(res_put[0], 200)
        res_get = ShopAPI.get_item_info("176")
        Checkings.check_status_code(res_get, 200)
        Checkings.check_keyword(res_get, True, "name", "НОСОЧКИ")
        Checkings.check_keyword(res_get, True, "section", "Платья")
        Checkings.check_keyword(res_get, True, "description", "Модное платье")
        Checkings.check_keyword(res_get, True, "size", "44")
        Checkings.check_keyword(res_get, True, "color", "GREEN")
        Checkings.check_keyword(res_get, True, "price", res_put[1])

    def test_update_item_incorrectId(self):
        res_put = ShopAPI.update_item_incorrectId("ff")
        Checkings.check_status_code(res_put, 200)
        Checkings.check_keyword(res_put, False, "status", "error")
        Checkings.check_keyword(res_put, False, "field_error", "id")
        Checkings.check_keyword(res_put, False, "error", "id_not_filled")
        Checkings.check_keyword(res_put, False, "message", "Поле ID товара заполнено не корректно")

    def test_update_item_emptyId(self):
        res_put = ShopAPI.update_item_incorrectId("")
        Checkings.check_status_code(res_put, 200)
        Checkings.check_keyword(res_put, False, "status", "error")
        Checkings.check_keyword(res_put, False, "field_error", "id")
        Checkings.check_keyword(res_put, False, "error", "id_not_filled")
        Checkings.check_keyword(res_put, False, "message", "Поле ID товара  не заполнено")