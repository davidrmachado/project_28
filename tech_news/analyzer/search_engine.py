from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    all_news = search_news({"title": {"$regex": title, "$options": "i"}})
    result = [(news["title"], news["url"]) for news in all_news]

    return result


# Requisito 8
def search_by_date(date):
    try:
        result = []

        new_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        news = search_news({"timestamp": new_date})

        for news in news:
            result.append((news['title'], news['url']))

        return result

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
