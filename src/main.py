import logging
from config import Config
import os
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types

bot = Bot(token=Config.bot_token)
dp = Dispatcher(bot)


async def on_startup(dispatcher) -> None:
    await bot.set_webhook(Config.webhook_url, drop_pending_updates=True)


async def on_shutdown(dispatcher) -> None:
    await bot.delete_webhook()


@dp.message_handler()
async def echo(message: types.Message) -> None:
    await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=Config.webhook_path,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=Config.webapp_host,
        port=Config.webapp_port,
    )
