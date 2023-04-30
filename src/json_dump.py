import requests
import json
from src.api_class import VacancyData
from src.vacancy import Vacancy


class JSONDump(VacancyData):
    """
    Класс для сохранения информации о вакансиях в json файл
    """
    def __init__(self, response: requests):
        self.response = response

    def add_vacancy(self, data, *args, **kwargs):
        """
        Запись данных в json файл
        """
        with open('vacancies.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_vacancies_list_hh(self):
        """
        Создание списка экземпляров класса для платформы HH
        :return: список экземпляров класса
        """
        with open('vacancies.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        vacancies = []
        for vacancy in data:
            if vacancy['salary'] is None:
                continue
            else:
                vacancies.append(
                    Vacancy(vacancy['id'], vacancy['name'], vacancy['alternate_url'], vacancy['salary']['from'],
                            vacancy['salary']['to'], vacancy['salary']['currency'],
                            vacancy['snippet']['responsibility']))
        return vacancies

    def get_vacancies_list_sj(self):
        """
        Создание списка экземпляров класса для платформы SJ
        :return: список экземпляров класса
        """
        with open('vacancies.json', 'r', encoding='utf-8') as file:
            data = json.load(file)['objects']

        vacancies = []
        for vacancy in data:
            if vacancy['payment_from'] is None:
                continue
            else:
                vacancies.append(Vacancy(vacancy['id'], vacancy['profession'], vacancy['link'], vacancy['payment_from'],
                                         vacancy['payment_to'], vacancy['currency'], vacancy['candidat']))
        return vacancies

    def selected_top(self, data, top_n):
        """
        Выборка по вакансиям топ№ через платформу HH
        :param top_n: сколько вакансий вывести
        :return: список вакансий по условиям выборки
        """
        return data[:int(top_n)]

    def selected_payment_min(self, data, payment_min=None):
        """
        Выборка по вакансиям с зп не менее заданного уровня через платформу HH
        :param payment_min: минимальный уровень зарплаты
        :return: список вакансий по условиям выборки
        """
        vacancies_payment = []
        if payment_min is not None:
            for i in data:
                if i.payment_min is not None:
                    if int(payment_min) <= int(i.payment_min):
                        vacancies_payment.append(i)
                    else:
                        continue
                else:
                    continue
        return vacancies_payment

    def delete_vacancy(self, vacancies, user_index=None):
        """
        Удаление экземпляра из списка по индексу, введенному пользователем
        :param vacancies: список экземпляров класса
        :param user_index: индекс, введенный пользователем
        :return: список вакансий без удаленного элемента
        """
        if user_index is not None:
            del vacancies[int(user_index)-1]
            return vacancies

    def sorted_vac_min(self, data):
        """
        Сортировка json файла по минимальной зарплате
        :return: сортированный файл
        """
        for i in data:
            if i.payment_min is None:
                i.payment_min = 0
        return sorted(data, key=lambda x: x.payment_min, reverse=True)
