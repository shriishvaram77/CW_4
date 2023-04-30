class Vacancy:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, id_vac, title, url, payment_min, payment_max, currency, responsibility):
        self.id_vac = id_vac
        self.title = title
        self.url = url
        self.payment_max = payment_max
        self.payment_min = payment_min
        self.currency = currency
        self.responsibility = responsibility

    def __str__(self):
        """
        Вывод информации для пользователя
        """
        payment_min = f'от {self.payment_min}' if self.payment_min else ''
        payment_max = f'до {self.payment_max}' if self.payment_max else ''
        return f"{self.id_vac}\n{self.title}\n{self.url}\n{payment_min} {payment_max} {self.currency}" \
               f"\n{self.responsibility}"

