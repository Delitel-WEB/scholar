import asyncio
from concurrent.futures import ThreadPoolExecutor

from scholarly import scholarly


async def get_russian_references(topic, num_results=10):  # noqa: ANN001, ANN201
    """
    Асинхронно получает список научных источников на русском языке по заданной теме.

    :param topic: Тема для поиска статей.
    :param num_results: Количество результатов.
    :return: Список найденных источников.
    """
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as executor:
        search_query = await loop.run_in_executor(executor, scholarly.search_pubs, topic)

        references = []
        count = 0

        for result in search_query:
            title = result['bib'].get('title', 'Без названия')
            authors = result['bib'].get('author', 'Неизвестные авторы')
            year = result['bib'].get('pub_year', 'Неизвестный год')
            link = result.get('pub_url', 'Ссылка отсутствует')

            references.append({
                'title': title,
                'authors': authors,
                'year': year,
                'link': link
            })

            count += 1
            if count >= num_results:
                break

        return references