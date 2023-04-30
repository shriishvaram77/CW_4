from abc import ABC, abstractmethod
import requests


class API(ABC):
    @abstractmethod
    def api(self, *args, **kwargs):
        """
        Абстрактный класс для работы с API
        """
        pass


class VacancyData(ABC):
    @abstractmethod
    def add_vacancy(self, params, api_url, *args, **kwargs):
        """
        Добавление вакансий в файл
        """
        pass

    @abstractmethod
    def selected_top(self, *args, **kwargs):
        """
        Вывод ТОП вакансий
        """
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs):
        """
        Удаление вакансии по порядковому номеру из списка
        """
        pass


class HH(API):
    def api(self, keyword) -> str:
        """
        Подключение по API
        :return: response
        """
        api_url = 'https://api.hh.ru/vacancies'
        params = {
            "text": keyword,
            "per_page": 10,
            "area": 145
        }
        response = requests.get(api_url, params=params, verify=False)

        if response.status_code == 200:
            vacancies = response.json()["items"]
            return vacancies
        else:
            return f'Error: {requests.get(api_url, params=params).status_code}'

    def get_vacancies(self, keyword):
        return self.api(keyword)


class SJ(API):
    def api(self, keyword):
        """
        Подключение по API
        :return: response
        """
        api_url = 'https://api.superjob.ru/2.0/vacancies/'
        params = {
            'keyword': keyword,
            'town': 'Санкт-Петербург',
            'count': 100,
            'period': 0
        }
        headers = {
            'X-Api-App-Id': 'v3.r.137494111.a6b43592ad3010404a6417932bb1b169d0bff73d.8da83ac6ac2fd9187fe1b5b8a7ecd1cc096ff71c',
            'Content-Type': 'application/json'
        }
        return requests.get(api_url, params=params, headers=headers, verify=False).json()

    def get_vacancies(self, keyword):
        """
        Возвращает вакансии по ключевому слову
        :param keyword: ключевое слово пользователя
        """
        return self.api(keyword)
