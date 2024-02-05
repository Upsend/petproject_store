from requests import Response
from utils.Checkings import Checkings
from utils.ShopAPI import ShopAPI

"""Запуск и проверка результатов тестов"""

class Test_item():


    def test_crete_new_item_full(self):
        res_post = ShopAPI.crete_new_item("full")
        Checkings.check_status_code(res_post, 200)
        Checkings.check_keyword(res_post, True, "name", "НОСОЧКИ")
        Checkings.check_keyword(res_post, True, "section", "Платья")
        Checkings.check_keyword(res_post, True, "description", "Модное платье")
        Checkings.check_keyword(res_post, True, "size", "44")
        Checkings.check_keyword(res_post, True, "color", "GREEN")
        Checkings.check_keyword(res_post, True, "price", 666)
        Checkings.check_keyword(res_post, True, "params", "dress")


    def test_create_new_item_short(self):
        res_post = ShopAPI.crete_new_item("short")
        Checkings.check_status_code(res_post, 200)
        Checkings.check_keyword(res_post, True, "name", "Шортики")
        Checkings.check_keyword(res_post, True, "section", "Платья")
        Checkings.check_keyword(res_post, True, "description", "Модное платье из новой коллекции!")

    def test_crete_new_item_short_name_err(self):
        res_post = ShopAPI.crete_new_item_short_err("name")
        Checkings.check_status_code(res_post, 200)
        Checkings.check_keyword(res_post, False, "status", "error")
        Checkings.check_keyword(res_post, False, "field_error", "name")
        Checkings.check_keyword(res_post, False, "error", "name_not_filled")
        Checkings.check_keyword(res_post, False, "message", "Название товара не заполнено!")


    def test_crete_new_item_short_section_err(self):
        res_post = ShopAPI.crete_new_item_short_err("section")
        Checkings.check_status_code(res_post, 200)
        Checkings.check_keyword(res_post, False, "status", "error")
        Checkings.check_keyword(res_post, False, "field_error", "section")
        Checkings.check_keyword(res_post, False, "error", "section_not_found")
        Checkings.check_keyword(res_post, False, "message", "Категория не найдена!")

    def test_crete_new_item_short_description_err(self):
        res_post = ShopAPI.crete_new_item_short_err("description")
        Checkings.check_status_code(res_post, 200)
        Checkings.check_keyword(res_post, False, "status", "error")
        Checkings.check_keyword(res_post, False, "field_error", "description")
        Checkings.check_keyword(res_post, False, "error", "description_not_found")
        Checkings.check_keyword(res_post, False, "message", "Описание не найдено!")

