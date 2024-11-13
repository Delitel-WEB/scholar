from aiogram.types import Message

from ..core import dp
from ..utils.recomendations import generate_recommendation
from ..utils.references import get_russian_references


@dp.message()
async def start(message: Message) -> None:
    search_message = await message.answer("Поиск источников...")

    references = await get_russian_references(message.text)
    references_text = ""

    for ref in references:
        references_text += f"Название: {ref['title']}\n"
        references_text += f"Авторы: {ref['authors']}\n"
        references_text += f"Год: {ref['year']}\n"
        references_text += f"Ссылка: <a href='{ref['link']}'>{ref['title']}</a>\n\n"


    await search_message.edit_text(
        f"Источники:\n\n{references_text}",
        parse_mode='html',
        disable_web_page_preview=False
    )

    recomendations_message = await message.answer("Подготавливаем рекомендации...\nЭто может занять время.")
    try:
        recomendations = await generate_recommendation(message.text, references)
        await recomendations_message.edit_text(
            recomendations,
            parse_mode="markdown"
        )
    except Exception as err:
        print(err)
        await recomendations_message.edit_text(
            "Не удалось подготовить рекомендации!"
        )

