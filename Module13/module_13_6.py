"""
Задача "Меньше текста, больше кликов":
Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий выдавались по нажатию
кнопки.

    Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на
    'Calories'.
    Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом: 'Рассчитать' и
    'Информация'. Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи параметра
    resize_keyboard.
    Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.

В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками. При нажатии на кнопку с надписью
'Рассчитать' срабатывает функция set_age с которой начинается работа машины состояний для age, growth и weight.
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
