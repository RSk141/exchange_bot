from aiogram import types
from loader import dp
from call_api import api
from utils.db_api.db_com import add_rate_data, get_rates
import datetime


@dp.message_handler(commands=['list', 'lst'])
async def show_list(message: types.Message):
    time = datetime.datetime.now()
    rates_list = await get_rates(time)
    await message.answer('<b>Here is a list of all the rates:</b>\n' + rates_list )