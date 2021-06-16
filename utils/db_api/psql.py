from aiogram import Dispatcher
from aiogram.utils.executor import Executor
from gino import Gino
from sqlalchemy import Column, sql

from data import config

db = Gino()


class Rate(db.Model):
    __tablename__ = 'rates'
    id = db.Column(db.Integer(), default=0)
    currency_data = db.Column(db.String(), default=None)
    timestamp = db.Column(db.Integer())


async def on_startup(dispatcher: Dispatcher):
    await db.set_bind(config.POSTGRES_URI)


def setup(executor: Executor):
    executor.on_startup(on_startup)
