from aiogram import Bot, Dispatcher, types
import asyncio
import logging
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from db import City, TypeEvent, Event, Organization
from aiogram import F, html

logging.basicConfig(level=logging.INFO)
bot = Bot(token='6456897497:AAG3YBuqFBij8zXmGG-A3b9UKcxcNLyKhcw')
dp = Dispatcher()

user_data = {}

@dp.message(Command('start'))
async def begin(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите город:', reply_markup=genmarkupcity())

@dp.callback_query(F.data.startswith("city_"))
async def get_city(callback: types.CallbackQuery):
    city_title = callback.data.split("_")[1]
    user_data["city"] = City.get(City.title == city_title)
    await bot.send_message(callback.from_user.id, 'Выберите тип события:', reply_markup=genmarkuptypes())

@dp.callback_query(F.data.startswith("type_"))
async def get_type_event(callback: types.CallbackQuery):
    type_title = callback.data.split("_")[1]
    user_data["type_event"] = TypeEvent.get(TypeEvent.title == type_title)
    events = Event.select().where((Event.city_id == user_data.get("city").id) & (Event.type_id == user_data.get("type_event").id) & (Event.is_active == True))
    for event in events:
        await callback.message.answer(f'<b>{event.title}</b>\n\n{event.description}\n\nВремя: {event.time_start}-{event.time_end}\nДата события: <b>{event.date_event}</b>', parse_mode="HTML",
                                      reply_markup=genmarkupevent(f"https://vinoevent.ru/events/{event.website_id}"))

async def change_city(message: types.Message):
    await message.answer("Выберете город")

def genmarkupevent(url):
    markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Подробнее", url=url)]])
    return markup

def genmarkuptypes():
    data = TypeEvent.select().execute()
    buttons = []
    for type_event in data:
        if Event.select().where((Event.type_id == type_event.id) & (Event.is_active == True) & (Event.city_id == user_data.get("city").id)).exists():
            buttons.append([InlineKeyboardButton(text=type_event.title,callback_data=f'type_{type_event.title}')])
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)
    return markup

def genmarkupcity():
    data = City.select().execute()
    buttons = []
    for city in data:
        buttons.append([InlineKeyboardButton(text=city.title,callback_data=f'city_{city.title}')])
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)
    return markup

async def main():
    await dp.start_polling(bot)

dp.message.register(change_city,Command('test'))

if __name__ =='__main__':
    asyncio.run(main())