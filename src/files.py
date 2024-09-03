import json
import os

from config import DATA_DIR
from src.vacansies import Vacansy


class WorkWithFile:
    """Класс, принимает название json файла с вакансиями (название также задано по-умолчанию).
    Читает указанный файл в папке data проекта,
    выводит список вакансий как в str виде так и в расширенном виде.
    Позволяет создавать и редактировать список вакансий - добавлять вакансии, удалять их по индексу.
    Изменённый список позволяет записать в заданный файл."""

    filename: str

    def __init__(self, filename="vacansies.json"):
        self.filename = filename
        self.fullname = os.path.join(DATA_DIR, filename)
        self.vacs_list = []

    def read_file(self) -> None:
        """Метод читает указанный файл и сохраняет список объектов вакансий из файла."""
        with open(self.fullname, "r", encoding="UTF-8") as file:
            temp_info = json.load(file)
        self.vacs_list = [Vacansy(**item) for item in temp_info]

    def show_vacansy_list(self):
        """Метод выводит расширенную информацию о вакансиях из списка объектов вакансий с номерами."""
        num = 0
        result_info = ""
        for item in self.vacs_list:
            num += 1
            result_info += f"Номер - {num} Вакансия: {item.title}, зарплата: {item.salary}, ссылка: {item.link}, описание: {item.description}, требования: {item.requirement}\n"
            return result_info

    def show_str_vacs(self):
        """Метод выводит сокращённую информацию о вакансиях из списка объектов вакансий с номерами."""
        num = 0
        result_info = ""
        for item in self.vacs_list:
            num += 1
            result_info += f"Номер - {num} {str(item)}\n"
        return result_info

    def show_vacansy_by_index(self, index):
        """Метод выводит расширенную информацию о вакансии по заданному индексу."""
        item = self.vacs_list[index - 1]
        return f"Вакансия: {item.title}, зарплата: {item.salary}, ссылка: {item.link}, описание: {item.description}, требования: {item.requirement}"

    def add_vacansy(self, vacansy: dict) -> None:
        """Метод добавляет объект вакансии в список вакансий, принимая данные в виде словаря с описанием вакансии."""
        new_vacansy = Vacansy(**vacansy)
        self.vacs_list.append(new_vacansy)

    def add_vacansy_object(self, vacansy: Vacansy) -> None:
        """Метод добавляет объект вакансии в список вакансий, принимая данные в объекта класса Vacansy."""
        self.vacs_list.append(vacansy)

    def add_vacansy_list(self, vac_list: list[Vacansy]) -> None:
        """Метод добавляет объекты вакансии в список вакансий, принимая данные в виде списка объектов класса Vacansy."""
        self.vacs_list.extend(vac_list)

    def add_vacansy_dicts(self, vac_dicts: list[dict]) -> None:
        """Метод добавляет объекты вакансии в список вакансий, принимая данные в виде списка словарей с описанием вакансий."""
        for vacansy in vac_dicts:
            new_vacansy = Vacansy(**vacansy)
            self.vacs_list.append(new_vacansy)

    def del_vacansy(self, number: int) -> None:
        """Метод удаляет из списка объект вакансии по номеру (индексу)."""
        self.vacs_list.pop(number - 1)

    def write_new_vac_list(self) -> None:
        """Метод записывает обработанный список вакансий в исходный файл, тем самым изменяя список в нём."""
        try:
            temp_vac_list = []
            for item in self.vacs_list:
                temp_vac_list.append(
                    {
                        "title": item.title,
                        "salary": item.salary,
                        "link": item.link,
                        "description": item.description,
                        "requirement": item.requirement,
                    }
                )
            with open(self.fullname, "w", encoding="utf-8") as file:
                json.dump(temp_vac_list, file, ensure_ascii=False, indent=4)
            print("Файл записан")
        except:
            raise ValueError("При записи фаайла произошла ошибка!")


if __name__ == "__main__":
    file = WorkWithFile("vacs.json")
    print(file.filename)
    # Чтение файла
    file.read_file()
    # Вывод считанного списка
    print(file.show_vacansy_list())
    # Удаление вакансии по индексу
    file.del_vacansy(0)
    # Вывод изменённого списка
    print(file.show_vacansy_list())

    vac1 = {
        "title": "Инженер 1 кат",
        "salary": 150000,
        "link": "https://steamcommunity.com/profiles/76561198140377023",
        "description": "Работа с технической документацией",
        "requirement": "Опрыт работы от 5 лет. Высшее образование.",
    }
    vac2 = {
        "title": "Инженер 2 кат",
        "salary": 70000,
        "link": "https://steamcommunity.com/profiles/76561198140377023",
        "description": "Работа с технической документацией",
        "requirement": "Опрыт работы от 2 лет. Высшее образование.",
    }
    # Добавление вакансии в виде словаря
    file.add_vacansy(vac1)
    print(file.show_vacansy_list())
    # Добавление вакансии в виде объекта Vacansy
    file.add_vacansy_object(Vacansy(**vac2))
    print(file.show_vacansy_list())
    # Добавление вакансий в виде списка словарей
    file.add_vacansy_dicts([vac1, vac2])
    print(file.show_vacansy_list())
    # Добавление вакансий в виде списка объектов Vacansy
    file.add_vacansy_list([Vacansy(**vac1), Vacansy(**vac2)])
    print(file.show_vacansy_list())
    # Запись отредактированного списка в файл
    file.write_new_vac_list()
    # Чтение файла
    file.read_file()
    # Вывод считанного списка
    print(file.show_str_vacs())
    # Вывод информации о вакансии по индексу
    print(file.show_vacansy_by_index(6))
