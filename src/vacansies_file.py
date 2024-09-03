import json
import os
from abc import ABC, abstractmethod

from config import DATA_DIR
from src.vacansies import Vacansy


class ReadWriteFile(ABC):
    """Абстрактный класс по чтению/записи файла."""

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self):
        pass

    @abstractmethod
    def export_vacansy_list(self):
        pass

    @abstractmethod
    def import_vacansy_list(self):
        pass

    @abstractmethod
    def del_data(self):
        pass


class VacansyFile(ReadWriteFile):
    """Класс работает с записью/чтением списка вакансий в файл, принимает/возвращает список вакансий.
    Родительский класс - ReadWriteFile."""

    filename: str

    def __init__(self, filename=DATA_DIR):
        self.filename = filename
        self.fullname = os.path.join(DATA_DIR, filename)
        self.vacs_list = []

    def read_file(self) -> None:
        """Метод читает указанный файл и сохраняет список объектов вакансий из файла."""
        with open(self.fullname, "r", encoding="UTF-8") as file:
            temp_info = json.load(file)
        self.vacs_list = [Vacansy(**item) for item in temp_info]

    def write_file(self) -> None:
        """Метод записывает обработанный список вакансий в исходный файл, тем самым изменяя список в нём."""
        try:
            temp_vac_list = []
            for item in self.vacs_list:
                temp_vac_list.append(
                    {
                        "title": item.title,
                        "salary": item.salary,
                        "area": item.area,
                        "description": item.description,
                        "requirement": item.requirement,
                        "link": item.link,
                    }
                )
            with open(self.fullname, "a", encoding="utf-8") as file:
                json.dump(temp_vac_list, file, ensure_ascii=False, indent=4)
            print("Файл успешно записан.")
        except Exception:
            raise ValueError("При записи файла произошла ошибка!")

    def export_vacansy_list(self):
        """Метод возвращает список объектов вакансий."""
        return self.vacs_list

    def import_vacansy_list(self, new_list):
        """Метод принимает новый список объектов вакансий и заменяет им старый."""
        self.vacs_list = new_list

    def del_data(self):
        """ Удаление данных из файла """

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
