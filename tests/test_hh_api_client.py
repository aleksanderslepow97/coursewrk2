from src.hh_api_client import HeadHunterAPI


def test_head_hunter_api():
    api = HeadHunterAPI()
    assert api.url == "https://api.hh.ru/vacancies"
    vacs = api.load_vacancies("python")
    assert len(vacs) == 2000
