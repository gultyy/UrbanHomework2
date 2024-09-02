"""
Задача "Цепочка вопросов":
Необходимо сделать цепочку обработки состояний для нахождения нормы калорий для человека.
Группа состояний:

    Импортируйте классы State и StateGroup из aiogram.dispatcher.filters.state.
    Создайте класс UserState наследованный от StateGroup.
    Внутри этого класса опишите 3 объекта класса State: age, growth, weight (возраст, рост, вес).

Эта группа(класс) будет использоваться в цепочке вызовов message_handler'ов. Напишите следующие функции для обработки
состояний:
Функцию set_age(message):

    Оберните её в message_handler, который реагирует на текстовое сообщение 'Calories'.
    Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:'.
    После ожидать ввода возраста в атрибут UserState.age при помощи метода set.

Функцию set_growth(message, state):

    Оберните её в message_handler, который реагирует на переданное состояние UserState.age.
    Эта функция должна обновлять данные в состоянии age на message.text (написанное пользователем сообщение).
    Используйте метод update_data.
    Далее должна выводить в Telegram-бот сообщение 'Введите свой рост:'.
    После ожидать ввода роста в атрибут UserState.growth при помощи метода set.

Функцию set_weight(message, state):

    Оберните её в message_handler, который реагирует на переданное состояние UserState.growth.
    Эта функция должна обновлять данные в состоянии growth на message.text (написанное пользователем сообщение).
    Используйте метод update_data.
    Далее должна выводить в Telegram-бот сообщение 'Введите свой вес:'.
    После ожидать ввода роста в атрибут UserState.weight при помощи метода set.

Функцию send_calories(message, state):

    Оберните её в message_handler, который реагирует на переданное состояние UserState.weight.
    Эта функция должна обновлять данные в состоянии weight на message.text (написанное пользователем сообщение).
    Используйте метод update_data.
    Далее в функции запомните в переменную data все ранее введённые состояния при помощи state.get_data().
    Используйте упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы калорий (для женщин или мужчин - на ваше
    усмотрение). Данные для формулы берите из ранее объявленной переменной data по ключам age, growth и weight
    соответственно.
    Результат вычисления по формуле отправьте ответом пользователю в Telegram-бот.
    Финишируйте машину состояний методом finish().

!В течение написания этих функций помните, что они асинхронны и все функции и методы должны запускаться с оператором
await.
"""
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью. Введи "Calories" чтобы узнать норму калорий')


@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f'Ваша норма калорий '
                         f'{10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) + 5}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
