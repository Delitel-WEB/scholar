import asyncio

from bot import handlers
from bot.core import bot, dp


async def main() -> None:
    await dp.start_polling(bot)


asyncio.run(main())
