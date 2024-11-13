from aiogram.filters import CommandStart
from aiogram.types import Message

from ..core import dp


@dp.message(CommandStart())
async def start(message: Message) -> None:

    await message.answer(
        "Привет!\n\nЯ — бот, который поможет тебе с научной литературой.\n\n"
        "Если тебе нужно найти источники или рекомендации для твоей курсовой, дипломной работы "
        "или любого другого научного проекта, просто напиши название темы или работы, и я "
        "высылаю тебе список научных источников, статей.\n\n"
        "Какую тему ты изучаешь?"
    )