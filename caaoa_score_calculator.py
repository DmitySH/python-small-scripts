import pandas as pd
from tabulate import tabulate
import re


def formula(contests, tests, kdz=10, pass_zeros=True):
    contests['Контесты'] = contests['Контесты'].str.replace(',', '.')
    tests['Тесты'] = tests['Тесты'].str.replace(',', '.')

    contests = contests.astype('float64')
    tests = tests.astype('float64')

    if pass_zeros:
        return float(contests.mean(axis=1) * 0.8 + tests.mean(axis=1) * 0.1 + \
                     kdz * 0.1)
    else:
        return float(
            contests.sum(axis=1) / 18 * 0.8 + tests.sum(
                axis=1) / 18 * 0.1 + kdz * 0.1)


df = pd.read_csv('tables/ПиАА 2021-2022 Ведомость - Основная ведомость.csv',
                 decimal=',')
df = df.infer_objects()

head = df.head(10)
surname = input('Введите фамилию: ')
pass_zeros = False if input(
    'Введите, нужно ли учитывать ненаписанные элементы (ставить вместо них ноль). yes если да, что угодно иначе: ').lower() == 'yes' else True
person = df[df['ФИО'].str.contains(rf'(?i){surname}|recess', na=False)]
contests = person.iloc[:, 4:22].dropna(axis=1)
tests = person.iloc[:, 22:39].dropna(axis=1)
print(formula(contests, tests, pass_zeros=pass_zeros))
