"""
Изменения в Telegram-бот:

    В самом начале запускайте ранее написанную функцию get_all_products.
    Измените функцию get_buying_list в модуле с Telegram-ботом, используя вместо обычной нумерации продуктов функцию
    get_all_products. Полученные записи используйте в выводимой надписи: "Название: <title> | Описание:
    <description> | Цена: <price>"

Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.
"""
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from curd_functions import *

initiate_db(db_name)
all_products = get_all_products(db_name)

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
bt1 = KeyboardButton(text='Рассчитать')
bt2 = KeyboardButton(text='Информация')
bt3 = KeyboardButton(text='Купить')
kb.add(bt1, bt2, bt3)

kbin = InlineKeyboardMarkup(
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


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет!', reply_markup=kb)


@dp.message_handler(text='Информация')
async  def info(message):
    await message.answer('Я бот помогающий твоему здоровью.\nЯ помогу рассчитать норму калорий.')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выбери опцию:', reply_markup=kbin)


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
    await UserState.age.set()
    await call.answer()


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