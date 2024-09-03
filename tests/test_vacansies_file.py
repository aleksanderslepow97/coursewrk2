from src.vacansies_file import VacansyFile


def test_vacansy_file_init(file_name):
    """Тестирование инициализации."""
    assert VacansyFile(file_name).filename == "test_file_name.json"


def test_vacansy_file_import_export(vacansy_list_for_filter):
    """Тестирование импорта и экспорта списка вакансий."""
    test = VacansyFile()
    test.import_vacansy_list(vacansy_list_for_filter)
    assert test.export_vacansy_list() == vacansy_list_for_filter
