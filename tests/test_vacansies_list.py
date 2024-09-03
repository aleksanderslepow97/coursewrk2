from src.vacansies_list import VacansyList


def test_vacansy_list_init():
    """Тестирование инициализации"""
    test = VacansyList()
    assert len(test.vacs_list) == 0


def test_vacansy_list_adding_vac(vacansy_1):
    """Тестирование добавления объекта вакансий в список."""
    test = VacansyList()
    test.add_vacansy(vacansy_1)
    assert test.show_vacansy_by_index(0) == vacansy_1.vac_full()


def test_vacansy_list_adding_list_obj(vacansy_list):
    """Тестирование добавления списка объектов вакансий в список."""
    test = VacansyList()
    test.add_vacansy(vacansy_list)
    assert test.show_str_vacs() == (
        "Номер - 1 Вакансия - Инженер, зарплата - 90000, местоположение - Москва, ссылка на вакансию - https://steamcommunity.com/profiles/76561198140377023.\n"
        "Номер - 2 Вакансия - Инженер, зарплата - 50000, местоположение - Москва, ссылка на вакансию - https://steamcommunity.com/profiles/76561198140377023.\n"
    )


def test_vacansy_list_export_import(vacansy_list):
    """Тестирование импорта и экспорта списка вакансий."""
    test = VacansyList()
    test.import_vacansy_list(vacansy_list)
    assert test.export_vacansy_list() == vacansy_list
    assert test.show_str_vacs() == (
        "Номер - 1 Вакансия - Инженер, зарплата - 90000, местоположение - Москва, ссылка на вакансию - https://steamcommunity.com/profiles/76561198140377023.\n"
        "Номер - 2 Вакансия - Инженер, зарплата - 50000, местоположение - Москва, ссылка на вакансию - https://steamcommunity.com/profiles/76561198140377023.\n"
    )
