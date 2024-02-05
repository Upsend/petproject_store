from requests import Response
from utils.Checkings import Checkings
from utils.ShopAPI import ShopAPI

"""Запуск и проверка результатов тестов"""

class Test_item:

    def test_full_cycle(self):
        #Создаем запись с помощью метода POST
        res_post = ShopAPI.crete_new_item("full")
        current_id = res_post.json()['result']['id']
        Checkings.check_status_code(res_post, 200)
        Checkings.check_keyword(res_post, True, "name", "НОСОЧКИ")
        Checkings.check_keyword(res_post, True, "section", "Платья")
        Checkings.check_keyword(res_post, True, "description", "Модное платье")
        Checkings.check_keyword(res_post, True, "size", "44")
        Checkings.check_keyword(res_post, True, "color", "GREEN")
        Checkings.check_keyword(res_post, True, "price", 666)
        Checkings.check_keyword(res_post, True, "params", "dress")
        #Получим данные по созданной записи с помощью метода GET
        res_get = ShopAPI.get_item_info(current_id)
        Checkings.check_status_code(res_get, 200)
        Checkings.check_keyword(res_get, True, "name", "НОСОЧКИ")
        Checkings.check_keyword(res_get, True, "section", "Платья")
        Checkings.check_keyword(res_get, True, "description", "Модное платье")
        Checkings.check_keyword(res_get, True, "size", "44")
        Checkings.check_keyword(res_get, True, "color", "GREEN")
        Checkings.check_keyword(res_get, True, "price", 666)
        #Обновим данные методом PUT
        res_put = ShopAPI.update_item_correct(current_id)
        Checkings.check_status_code(res_put[0], 200)
        res_get = ShopAPI.get_item_info(current_id)
        Checkings.check_status_code(res_get, 200)
        Checkings.check_keyword(res_get, True, "name", "НОСОЧКИ")
        Checkings.check_keyword(res_get, True, "section", "Платья")
        Checkings.check_keyword(res_get, True, "description", "Модное платье")
        Checkings.check_keyword(res_get, True, "size", "44")
        Checkings.check_keyword(res_get, True, "color", "GREEN")
        Checkings.check_keyword(res_get, True, "price", res_put[1])
        # Проверим что данные обновились с помощью метода GET
        res_get = ShopAPI.get_item_info(current_id)
        Checkings.check_status_code(res_get, 200)
        Checkings.check_keyword(res_get, True, "name", "НОСОЧКИ")
        Checkings.check_keyword(res_get, True, "section", "Платья")
        Checkings.check_keyword(res_get, True, "description", "Модное платье")
        Checkings.check_keyword(res_get, True, "size", "44")
        Checkings.check_keyword(res_get, True, "color", "GREEN")
        Checkings.check_keyword(res_get, True, "price", res_put[1])
        #Удалим запись методом Delete
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


