from aiogram import Bot, Dispatcher, types
import asyncio
import logging
from aiogram import F, html
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from sele import parsing_tt
import datetime

logging.basicConfig(level=logging.INFO)
bot = Bot(token='6604735280:AAG4hj-6MSPzgsCySsGqVFl2K0kJRGh0aKM')
dp = Dispatcher()

user_data = {}

@dp.message(Command('start'))
async def begin(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите через запятую аккаунты (например: https://www.tiktok.com/account1, https://www.tiktok.com/account2):')

@dp.message(F.text)
async def echo_with_time(message: Message):
    if message.text[:4] == "http":
        print("yea")
        urls = message.text.split(",")
        user_data["urls"] = urls
        print(urls)
        await message.answer(f"Введите период (Пример: 01.01.2023 - 02.02.2023)", parse_mode="HTML")
    else:
        print(message.text.split("-"))
        new_range_from = datetime.datetime.strptime(message.text.split("-")[0], '%d.%m.%Y ')
        new_range_to = datetime.datetime.strptime(message.text.split("-")[1], ' %d.%m.%Y')
        user_data["range_from"] = new_range_from
        user_data["range_to"] = new_range_to
        buttons = [[InlineKeyboardButton(text="Начать парсинг", callback_data='start_parsing')]]
        markup = InlineKeyboardMarkup(inline_keyboard=buttons)
        await bot.send_message(message.from_user.id, 'Нажмите на кнопку, чтобы начать парсниг', reply_markup=markup)

@dp.callback_query(F.data == "start_parsing")
async def get_city(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, f'Парсинг начат. Период: {user_data.get("range")}')

async def main():
    await dp.start_polling(bot)


if __name__ =='__main__':
    asyncio.run(main())