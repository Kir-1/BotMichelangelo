import asyncio
import logging
from config import Config
#from src.config_test import ConfigTest
import os
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# webhook
storage = MemoryStorage()
bot = Bot(token=Config.bot_token)
dp = Dispatcher(bot=bot, storage=storage)


if __name__ == '__main__':
    try:
        print("Bot started")
        from handlers import dp, bot
        from handlers.startup_shutdown import on_startup, on_shutdown

        try:
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
        finally:
            bot.get_session().close()
    except(KeyboardInterrupt, SystemExit):
        print('Bot stopped!')

# storage = MemoryStorage()
# bot = Bot(token=ConfigTest.bot_token)
# dp = Dispatcher(bot=bot, storage=storage)
#
#
# async def main() -> None:
#     from handlers import dp
#     try:
#         await dp.start_polling()
#     finally:
#         bot.get_session().close()
#
#
# if __name__ == '__main__':
#     try:
#         print("Bot started")
#         asyncio.run(main())
#     except(KeyboardInterrupt, SystemExit):
#         print('Bot stopped!')
