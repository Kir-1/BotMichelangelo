from src.config import Config
from src.main import bot, dp


async def on_startup(dispatcher) -> None:
    await bot.set_webhook(Config.webhook_url, drop_pending_updates=True)


async def on_shutdown(dispatcher) -> None:
    await bot.delete_webhook()