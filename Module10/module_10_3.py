"""
Задача "Банковские операции":
Необходимо создать класс Bank со следующими свойствами:

Атрибуты объекта:
balance - баланс банка (int)
lock - объект класса Lock для блокировки потоков.

Методы объекта:
Метод deposit:

    Будет совершать 100 транзакций пополнения средств.
    Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
    Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
    После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
    Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.

Метод take:

    Будет совершать 100 транзакций снятия.
    Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
    В начале должно выводится сообщение "Запрос на <случайное число>".
    Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив
    balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
    Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и
    заблокировать поток методом acquiere.

Далее создайте объект класса Bank и создайте 2 потока для его методов deposit и take. Запустите эти потоки.
После конца работы потоков выведите строку: "Итоговый баланс: <баланс объекта Bank>".
"""
from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            rep_amount = randint(50, 500)  # replenishment amount
            self.balance += rep_amount
            print(f'Пополнение: {rep_amount}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        cnt = 100
        while cnt > 0:
            wit_amount = randint(50, 500)  # withdrawal amount
            print(f'Запрос на {wit_amount}')
            if wit_amount <= self.balance:
                self.balance -= wit_amount
                print(f'Снятие: {wit_amount}. Баланс: {self.balance}')
                cnt -= 1
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
