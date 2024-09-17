from src.utils import get_top_vacancies, get_vacancies_by_salary_from, sort_vacancies_by_salary
from src.vacancy import Vacancy


def test_get_vacancies_by_salary_from(vacancies_objects):
    assert get_vacancies_by_salary_from(vacancies_objects, 500000) == []
    assert get_vacancies_by_salary_from(vacancies_objects, 100000) == [
        Vacancy("Разработчик", "https://hh", "требования", "обязанности", 100000)
    ]


def test_get_vacancies_by_salary_from_empty_list(vacancies_objects):
    assert get_vacancies_by_salary_from([], 1000000) == []


def test_get_vacancies_by_salary_from_0(vacancies_objects):
    assert get_vacancies_by_salary_from(vacancies_objects, 0) == vacancies_objects


def test_sort_vacancies_by_salary(vacancies_objects):
    res = sort_vacancies_by_salary(vacancies_objects)
    assert res[0].name == "Разработчик"
    assert res[3].name == "Разработчик1"


def test_sort_vacancies_by_salary_same_salary():
    vacs = [
        Vacancy("Разработчик", "https://hh", "требования", "обязанности", 100000),
        Vacancy("Разработчик2", "https://hh2", "требования 2", "обязанности 2", 100000),
        Vacancy("Разработчик1", "https://hh1", "требования 1", "обязанности 1", 10000),
    ]
    res = sort_vacancies_by_salary(vacs)

    assert res == [
        Vacancy("Разработчик", "https://hh", "требования", "обязанности", 100000),
        Vacancy("Разработчик2", "https://hh2", "требования 2", "обязанности 2", 100000),
        Vacancy("Разработчик1", "https://hh1", "требования 1", "обязанности 1", 10000),
    ]


def test_sort_vacancies_by_salary_empty_list():
    res = sort_vacancies_by_salary([])
    assert res == []


def test_get_top_vacancies(vacancies_objects):
    res = get_top_vacancies(vacancies_objects, 2)
    assert res == [
        Vacancy("Разработчик", "https://hh", "требования", "обязанности", 100000),
        Vacancy("Разработчик2", "https://hh", "требования 2", "обязанности 2", 50000),
    ]


def test_get_top_vacancies_empty_list():
    res = get_top_vacancies([], 2)
    assert res == []


def test_get_top_vacancies_top_n_0(vacancies_objects):
    res = get_top_vacancies(vacancies_objects, 0)
    assert res == []
