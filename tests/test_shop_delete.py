from requests import Response
from utils.Checkings import Checkings
from utils.ShopAPI import ShopAPI

"""Запуск и проверка результатов тестов с методом DELETE"""

class Test_item_del():

    def test_delete_correct(self):
        #Удалим запись методом Delete
        current_id = "250"
        res_del = ShopAPI.delete_item(current_id)
        Checkings.check_status_code(res_del, 200)
        Checkings.check_keyword(res_del, False, "status", "ok")
        Checkings.check_keyword(res_del, False, "result", f"Товар с ID {current_id} успешно удален")
        #Проверим, что данные удалились
        res_get = ShopAPI.get_item_info(current_id)
        Checkings.check_status_code(res_get, 200)
        Checkings.check_keyword(res_get, False, "status", "error")
        Checkings.check_keyword(res_get, False, "field_error", "id")
        Checkings.check_keyword(res_get, False, "error", "item_with_id_not_found")
        Checkings.check_keyword(res_get, False, "message", f"Товар с ID {current_id} не найден!")

    def test_delete_emptyId(self):
        # Удалим запись методом Delete
        current_id = ""
        res_del = ShopAPI.delete_item(current_id)
        Checkings.check_status_code(res_del, 200)
        Checkings.check_keyword(res_del, False, "status", "error")
        Checkings.check_keyword(res_del, False, "field_error", "id")
        Checkings.check_keyword(res_del, False, "error", "id_not_filled")
        Checkings.check_keyword(res_del, False, "message", f"Поле ID товара  не заполнено")

    def test_delete_unrealId(self):
        # Удалим запись методом Delete
        current_id = "444444444"
        res_del = ShopAPI.delete_item(current_id)
        Checkings.check_status_code(res_del, 200)
        Checkings.check_keyword(res_del, False, "status", "error")
        Checkings.check_keyword(res_del, False, "field_error", "id")
        Checkings.check_keyword(res_del, False, "error", "item_with_id_not_found")
        Checkings.check_keyword(res_del, False, "message", f"Товар с ID {current_id} не найден!")


