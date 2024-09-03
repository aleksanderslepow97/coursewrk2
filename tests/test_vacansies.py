def test_vacansy_init(vacansy_1):
    """Тестирование инициализации."""
    assert vacansy_1.title == "Инженер"
    assert vacansy_1.link == "https://steamcommunity.com/profiles/76561198140377023"
    assert vacansy_1.salary == 50000
    assert vacansy_1.area == "Москва"
    assert vacansy_1.description == "Работа с технической документацией"
    assert vacansy_1.requirement == "Опрыт работы от 3 лет. Высшее образование."
    assert (
        str(vacansy_1)
        == "Вакансия - Инженер, зарплата - 50000, местоположение - Москва, ссылка на вакансию - https://steamcommunity.com/profiles/76561198140377023."
    )


def test_vacansy_comparision(vacansy_1, vacansy_2):
    """Тестирование операций сравнения вакансий по размеру зарплаты."""
    assert vacansy_1 < vacansy_2
    assert vacansy_2 >= vacansy_1
