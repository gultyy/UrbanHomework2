"""
Задача "Продуктовая база":
Подготовка:
Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.

Дополните ранее написанный код для Telegram-бота:
Создайте файл crud_functions.py и напишите там следующие функции:
initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса. Эта таблица должна
содержать следующие поля:

    id - целое число, первичный ключ
    title(название продукта) - текст (не пустой)
    description(описание) - тест
    price(цена) - целое число (не пустой)

get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
"""
import sqlite3

db_name = 'bot_products.db'


def initiate_db(db):
    with open(db_name, 'w'):
        pass

    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    """)

    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Продукт{i}', f'Описание{i}', i*100))

    connection.commit()
    connection.close()


def get_all_products(db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    all_pro = cursor.fetchall()
    connection.close()
    return all_pro


if __name__ == '__main__':
    initiate_db(db_name)
    print(get_all_products(db_name))
