"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import hashlib
import csv

# Создаем файл БД логинов и хешей паролей
with open("bd.csv", mode="w", encoding='utf-8') as bd:
    file_writer = csv.writer(bd, delimiter="\t", lineterminator="\n")
    file_writer.writerow(["Login", "Password"])

# Регистрация пользователя
login = input('Введите имя пользователя: ')
with open("bd.csv", encoding='utf-8') as bd:
    f = csv.reader(bd, delimiter="\t")
    x = []
    for row in f:
        x.append(row[0])
    if login in x:
        print('Пользователь с таким именем уже существует. Придумайте уникальный логин')
    else:
        password = input('Введите пароль: ')
        hash = hashlib.sha256(login.encode() + password.encode()).hexdigest()
        with open("bd.csv", mode="a", encoding='utf-8') as file:
            file_writer = csv.writer(file, delimiter="\t", lineterminator="\n")
            file_writer.writerow([login, hash])
        print(f"Пользователь '{login}' успешно зарегистрирован")

# Авторизация пользователя
login = input('Введите имя пользователя: ')
password = input('Введите пароль: ')
with open("bd.csv", encoding='utf-8') as bd:
    f = csv.reader(bd, delimiter="\t")
    y = []
    for row in f:
        y.append(row[1])
    if hashlib.sha256(login.encode() + password.encode()).hexdigest() not in y:
        print('В доступе отказано. Неверное имя или пароль')
    else:
        print(f"Пользователь '{login}', вы ввели правильный пароль!")
