"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return self.date

    @classmethod
    def extract(cls, date):
        day, month, year = map(int, date.split('-'))
        return f'{day}-{month}-{year}'

    @staticmethod
    def validation(day, month, year):
        if day < 1 or day > 31:
            print(f'В месяце 30/31 день. Числа {day} не существует')
        if month < 1 or month > 12:
            print(f'Месяца под номером {month} не существует')
        if year > 2021:
            print(f'{year} год еще не наступил')


date_1 = Date('29-6-2021')
print(date_1)

print(Date.extract('29-6-2021'))
Date.validation(35, 13, 2022)
