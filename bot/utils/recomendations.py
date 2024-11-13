from ..core import client


async def generate_recommendation(topic, references) -> str:  # noqa: ANN001
    """
    Генерирует рекомендации для курсовой работы на основе полученных источников.

    :param topic: Тема курсовой работы.
    :param references: Список источников.
    :return: Рекомендация для курсовой работы.
    """
    sources_text = "\n".join([f"{i+1}. {ref['title']} - {ref['authors']} ({ref['year']})"for i, ref in enumerate(references)])
    prompt = f"Тема курсовой работы: {topic}\nИсточники:\n{sources_text}\n\nСформулируй рекомендации для написания\n" \
             "курсовой работы, основываясь на этих источниках. Напиши ТОЛЬКО рекомендации! НА РУССКОМ ЯЗЫКЕ!"

    recommendation = await client.chat.completions.async_create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
)
    return recommendation.choices[0].message.content
