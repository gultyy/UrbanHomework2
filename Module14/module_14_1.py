"""
Задача "Первые пользователи":
Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:

    id - целое число, первичный ключ
    username - текст (не пустой)
    email - текст (не пустой)
    age - целое число
    balance - целое число (не пустой)

Заполните её 10 записями:
User1, example1@gmail.com, 10, 1000
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 1000
...
User10, example10@gmail.com, 100, 1000
Обновите balance у каждой 2ой записи начиная с 1ой на 500:
User1, example1@gmail.com, 10, 500
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 500
...
User10, example10@gmail.com, 100, 1000
Удалите каждую 3ую запись в таблице начиная с 1ой:
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 500
User5, example5@gmail.com, 50, 500
...
User9, example9@gmail.com, 90, 500

Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем
формате (без id):
Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
"""
import sqlite3

# with open('not_telegram.db', 'w'):
#     pass

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

users_amount = 10

for i in range(1, users_amount + 1):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}',
                                                                                             f'example{i}@gmail.com',
                                                                                             i*10, 1000))

new_balance = 500

for i in range(1, users_amount + 1, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (new_balance, f'User{i}'))

for i in range(1, users_amount + 1, 3):
    cursor.execute('DELETE FROM USERS WHERE USERNAME = ?', (f'User{i}', ))

cursor.execute('SELECT * FROM Users WHERE age != ?', (60, ))
users = cursor.fetchall()

for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

connection.commit()
connection.close()



