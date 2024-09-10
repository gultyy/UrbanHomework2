"""
Задача "Регистрация покупателей":
Подготовка:
Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.

Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:
initiate_db дополните созданием таблицы Users, если она ещё не создана при помощи SQL запроса. Эта таблица должна
содержать следующие поля:

    id - целое число, первичный ключ
    username - текст (не пустой)
    email - текст (не пустой)
    age - целое число (не пустой)
    balance - целое число (не пустой)

add_user(username, email, age), которая принимает: имя пользователя, почту и возраст. Данная функция должна
добавлять в таблицу Users вашей БД запись с переданными данными. Баланс у новых пользователей всегда равен 1000. Для
добавления записей в таблице используйте SQL запрос.
is_included(username) принимает имя пользователя и возвращает True, если такой пользователь есть в таблице Users,
в противном случае False. Для получения записей используйте SQL запрос.
"""
import sqlite3

db_products = 'bot_products.db'
db_users = 'bot_user.db'

with open(db_products, 'w'):
    pass
connection1 = sqlite3.connect(db_products)
cursor1 = connection1.cursor()

with open(db_users, 'w'):
    pass
connection2 = sqlite3.connect(db_users)
cursor2 = connection2.cursor()


def initiate_db():
    cursor1.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    """)
    for i in range(1, 5):
        cursor1.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                        (f'Продукт{i}', f'Описание{i}', i * 100))
    connection1.commit()

    cursor2.execute("""
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        """)
    connection2.commit()


def get_all_products(db):
    cursor1.execute('SELECT * FROM Products')
    all_pro = cursor1.fetchall()
    return all_pro


# def add_user(username, email, age):
#     cursor2.execute(f'INSERT INTO Users (username, email, age, balance) VALUES({username}, {email}, {age}, 1000) ')
#     connection2.commit()

def add_user(username, email, age):
    cursor2.execute(f'INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                    (username, email, age, 1000))
    connection2.commit()


def is_included(username):
    return (username, ) in cursor2.execute('SELECT username FROM Users').fetchall()

