import datetime

from aiogram import types

from call_api import api
from loader import dp

import os

from plot import build_plot


@dp.message_handler(commands='history')
async def exchange(message: types.Message):
    args = message.get_args().split()
    if len(args) != 4:
        await message.answer("Please, use the correct format. Ex: /history USD/CAD for 7 days")
    else:
        curr = args[0].replace('/', '')
        amount = int(args[2])
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=amount)
        history = api().get_history(curr, start_date, end_date)
        try:
            path = build_plot(history, curr)
            await message.answer_photo(types.InputFile(path))
            os.remove(path)
        except:
            await message.answer('No exchange rate data is available for the selected currency.')
