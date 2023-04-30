from src.api_class import HH, SJ
from src.json_dump import JSONDump
from src.user import USER


def main():
    platform = input('Выберите платформу для поиска вакансий: (HeadHunter / SuperJob): ')
    keyword = input('Введите ключевое слово для поиска ваканций: ')
    top_n = input("Введите количество вакансий для вывода: ")
    payment_min = input('Введите минимальный уровень зарплаты: ')

    user = USER(platform, keyword, top_n, payment_min)
    json_saver = JSONDump(user.keyword)

    if user.platform == 'HeadHunter':
        hh_api = HH()
        hh_vacancies = hh_api.get_vacancies(user.keyword)
        json_saver.add_vacancy(hh_vacancies)
        data = json_saver.get_vacancies_list_hh()
        data = json_saver.sorted_vac_min(data)
        if payment_min != '':
            data = json_saver.selected_payment_min(data, payment_min)
        if top_n != '':
            data = json_saver.selected_top(data, user.top_n)

        for row in data:
            print(row, end='\n\n')

        user_id = input('Удалить вакансию из списка по порядковому номеру: ')
        if user_id != '':
            data = json_saver.delete_vacancy(data, user_id)
            for row in data:
                print(row, end='\n\n')
        else:
            quit()

    elif user.platform == 'SuperJob':
        superjob_api = SJ()
        superjob_vacancies = superjob_api.get_vacancies(user.keyword)
        json_saver.add_vacancy(superjob_vacancies)
        data = json_saver.get_vacancies_list_sj()
        data = json_saver.sorted_vac_min(data)
        if payment_min != '':
            data = json_saver.selected_payment_min(data, payment_min)
        if top_n != '':
            data = json_saver.selected_top(data, user.top_n)

        for row in data:
            print(row, end='\n\n')

        user_id = input('Удалить вакансию из списка по порядковому номеру: ')
        if user_id != '':
            data = json_saver.delete_vacancy(data, user_id)
            for row in data:
                print(row, end='\n\n')
        else:
            quit()

    else:
        print('Нет данных по вашему запросу.')


if __name__ == "__main__":
    main()
