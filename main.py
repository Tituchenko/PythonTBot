from aiogram.utils import executor
from commands import dp
import logging


async def bot_start(_):
    print('Бот запущен!')



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True, on_startup=bot_start)