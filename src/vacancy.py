class Vacancy:
    """Класс для представления вакансий"""

    __slots__ = ("name", "url", "requirement", "responsibility", "salary")

    def __init__(self, name: str, url: str, requirement: str, responsibility: str,
                 salary: int | None = None) -> None:
        """Инициализатор класса Vacancy"""
        self.name = name
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        self.salary = self.__salary_validation(salary)

    @staticmethod
    def __salary_validation(salary: int | float | None) -> int | float | None:
        """Валидация зарплаты"""
        if salary:
            return salary
        return 0

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list["Vacancy"]:
        """Возвращает список экземпляров Vacancy из списка словарей"""

        return [cls(**vac) for vac in vacancies]

    def __str__(self) -> str:
        """Метод строкового предсиавления вакансий"""

        return (
            f"{self.name} (Зарплата: {self.salary if self.salary else 'не указана'}).\n"
            f"Требования: {self.requirement}.\nОбязанности: {self.responsibility}.\nСсылка на вакансию: {self.url}"
        )

    def __eq__(self, other) -> bool:
        """Метод сравнения вакансий (=)"""
        return self.salary == other.salary

    def __lt__(self, other) -> bool:
        """Метод сравнения вакансий (<)"""
        return self.salary < other.salary

    def __le__(self, other) -> bool:
        """Метод сравнения вакансий (<=)"""
        return self.salary <= other.salary

    def to_dict(self) -> dict:
        """Возвращает словарь с данными о вакансии из экземпляра класса Vacancy"""
        return {
            "name": self.name,
            "url": self.url,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
            "salary": self.salary,
        }
