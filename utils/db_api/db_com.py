import datetime

from utils.db_api.psql import Rate
from call_api import api


async def add_rate_data(data, timestamp: int):
    await Rate.update.values(currency_data=data, timestamp=timestamp).where(Rate.id == 0).gino.status()


async def get_rates(now_time):
    timestamp = await Rate.select('timestamp').where(Rate.id == 0).gino.scalar()
    data_time = datetime.datetime.fromtimestamp(timestamp)
    delta = now_time - data_time
    if delta.seconds < 600:
        prices = await Rate.select('currency_data').where(Rate.id == 0).gino.scalar()
    else:
        rates = api().process_rates()
        prices = '\n'.join(rates[0])
        await add_rate_data(prices, rates[1])
    return prices

