"""
Фукнции цепочки состояний RegistrationState:
sing_up(message):

    Оберните её в message_handler, который реагирует на текстовое сообщение 'Регистрация'.
    Эта функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
    После ожидать ввода возраста в атрибут RegistrationState.username при помощи метода set.

set_username(message, state):

    Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
    Функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
    Если пользователя message.text ещё нет в таблице, то должны обновляться данные в состоянии username на
    message.text.  Далее выводится сообщение "Введите свой email:" и принимается новое состояние
    RegistrationState.email.
    Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует, введите другое имя"
    и  запрашивать новое состояние для RegistrationState.username.

set_email(message, state):

    Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
    Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
    Далее выводить сообщение "Введите свой возраст:":
    После ожидать ввода возраста в атрибут RegistrationState.age.

set_age(message, state):

    Оберните её в message_handler, который реагирует на состояние RegistrationState.age.
    Эта функция должна обновляться данные в состоянии RegistrationState.age на message.text.
    Далее брать все данные (username, email и age) из состояния и записывать в таблицу Users при помощи ранее
    написанной  crud-функции add_user.
    В конце завершать приём состояний при помощи метода finish().

Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.
"""
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from curd_functions import *

initiate_db()
all_products = get_all_products(db_products)

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')],
        [KeyboardButton(text='Регистрация')]
    ],
    resize_keyboard=True)


kbin_calories = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ],
    resize_keyboard=True)

kbin_products = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
    ],
    resize_keyboard=True)


class CaloriesInfoState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет!', reply_markup=kb)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Я бот помогающий твоему здоровью.\nЯ помогу рассчитать норму калорий.')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выбери опцию:', reply_markup=kbin_calories)


@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer('Пользователь существует, введите другое имя')
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    user_data = await state.get_data()
    add_user(user_data["username"], user_data["email"], user_data["age"])
    await message.answer('Регистрация прошла успешно')
    await state.finish()


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    files = ['1.jpeg', '2.png', '3.jpg', '4.png']
    for i, f_name in zip(range(len(files)), files):
        with open(f'images/{f_name}', 'rb') as img:
            await message.answer(f'Название: {all_products[i][1]} | Описание: {all_products[i][2]} | Цена: '
                                 f'{all_products[i][3]}')
            await message.answer_photo(img)
    await message.answer('Выберете продукт для покупки:', reply_markup=kbin_products)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт')
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес(кг) + 6,25 х рост(см) - 5 х возраст(г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await CaloriesInfoState.age.set()
    await call.answer()


@dp.message_handler(state=CaloriesInfoState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await CaloriesInfoState.growth.set()


@dp.message_handler(state=CaloriesInfoState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await CaloriesInfoState.weight.set()


@dp.message_handler(state=CaloriesInfoState.weight)
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
