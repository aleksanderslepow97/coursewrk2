from src.hh_api_client import HHAPIClient


def user_interaction() -> None:
    # PRIMARY INPUT
    print('Greetings!')
    search_query = input('Enter your query:\n')
    top_n = input('Enter the number of vacancies to display:\n')

    # Creating client
    hh_client = HHAPIClient()

    # Casting Vacancies
    hh_vacancies = hh_client.load_vacancies(search_query)
    print(hh_vacancies)

if __name__ == '__main__':
    user_interaction()
