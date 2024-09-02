"""
Задача "Ещё больше выбора":
Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:

    С текстом 'Рассчитать норму калорий' и callback_data='calories'
    С текстом 'Формулы расчёта' и callback_data='formulas'

Создайте новую функцию main_menu(message), которая:

    Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
    Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'

Создайте новую функцию get_formulas(call), которая:

    Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
    Будет присылать сообщение с формулой Миффлина-Сан Жеора.

Измените функцию set_age и декоратор для неё:

    Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
    Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.

По итогу получится следующий алгоритм:

    Вводится команда /start
    На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
    В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
    По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
    По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.
"""
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
bt1 = KeyboardButton(text='Рассчитать')
bt2 = KeyboardButton(text='Информация')
kb.add(bt1, bt2)

kbin = InlineKeyboardMarkup(resize_keyboard=True)
btin1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
btin2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kbin.add(btin1, btin2)


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
