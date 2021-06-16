from aiogram import executor

from loader import dp
import handlers
from utils.db_api import psql
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.psql import db


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

    # Send message to admin
    await on_startup_notify(dispatcher)

    # connecting to DB
    await psql.on_startup(dp)

    # drop tables
    # await db.gino.drop_all()

    # create tables
    await db.gino.create_all()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
