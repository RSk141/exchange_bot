from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start the bot"),
            types.BotCommand("help", "Show info"),
            types.BotCommand("list", "Show rates list"),
            types.BotCommand("lst", "Show rates list"),
            types.BotCommand("exchange", "Exchange currency. ex: /exchange 10 USD to CAD"),
            types.BotCommand("history", "Show a graph which shows the exchange rate. ex: /history USD/CAD for 7 days")
        ]
    )
