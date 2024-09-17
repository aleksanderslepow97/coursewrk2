from src.vacancy import Vacancy


def test_vacancy_init():
    vac = Vacancy("Разработчик", "https://hh", "требования", "обязанности")
    assert vac.name == "Разработчик"
    assert vac.url == "https://hh"
    assert vac.requirement == "требования"
    assert vac.responsibility == "обязанности"
    assert vac.salary == 0


def test_cast_to_object_list(vacancies_dict):
    vacs = Vacancy.cast_to_object_list(vacancies_dict)
    assert len(vacs) == 2
    assert vacs[0].name == "Разработчик"
    assert vacs[1].salary == 120000


def test_cast_to_object_list_empty_list():
    vacs = Vacancy.cast_to_object_list([])
    assert vacs == []


def test_vacancy_str_salary_0():
    vac = Vacancy("Разработчик", "https://hh", "требования", "обязанности")
    assert str(vac) == (
        "Разработчик (Зарплата: не указана).\nТребования: требования.\n"
        "Обязанности: обязанности.\nСсылка на вакансию: https://hh"
    )


def test_vacancy_str():
    vac = Vacancy("Разработчик", "https://hh", "требования", "обязанности", 10000)
    assert str(vac) == (
        "Разработчик (Зарплата: 10000).\nТребования: требования.\n"
        "Обязанности: обязанности.\nСсылка на вакансию: https://hh"
    )


def test_vacancy_eq(vacancies_objects):
    vac = Vacancy("Разработчик", "https://hh", "требования", "обязанности")
    assert vacancies_objects[0] != vacancies_objects[1]
    assert vacancies_objects[1] == vac


def test_vacancy_lt(vacancies_objects):
    assert vacancies_objects[0] > vacancies_objects[1]
    assert vacancies_objects[2] < vacancies_objects[0]


def test_vacancy_le(vacancies_objects):
    assert vacancies_objects[0] >= vacancies_objects[1]
    assert vacancies_objects[2] <= vacancies_objects[0]


def test_vacancy_to_dict(vacancies_objects):
    vac = vacancies_objects[0]
    assert vac.to_dict() == {
        "name": "Разработчик",
        "url": "https://hh",
        "requirement": "требования",
        "responsibility": "обязанности",
        "salary": 100000,
    }

    vac = Vacancy("Разработчик", "https://hh", "требования", "обязанности")
    assert vac.to_dict() == {
        "name": "Разработчик",
        "url": "https://hh",
        "requirement": "требования",
        "responsibility": "обязанности",
        "salary": 0,
    }
