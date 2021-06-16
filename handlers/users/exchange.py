from aiogram import types

from call_api import api
from loader import dp


@dp.message_handler(commands='exchange')
async def exchange(message: types.Message):
    args = message.get_args().split()
    if len(args) != 4:
        await message.answer("Please, use the correct format. Ex: /exchange 10 USD to CAD")
    else:
        amount = args[0]
        from_curr = args[1]
        to_curr = args[3]
        price = api().convert_curr(from_curr, to_curr, amount)
        await message.answer(str(price) + ' ' + to_curr)
