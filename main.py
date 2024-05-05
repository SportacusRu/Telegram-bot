from src.client import SportacusClient
from src.bot.bot import dp

from aiogram import Bot
from src.config import TOKEN


if __name__ == "__main__":
    bot = Bot(TOKEN)
    dp.run_polling(bot)