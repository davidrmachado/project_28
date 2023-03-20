import requests
import time
import parsel
import re
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=headers, timeout=5)
    except (requests.HTTPError, requests.exceptions.Timeout):
        return None
    else:
        if response.status_code == 200:
            return response.text
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = parsel.Selector(html_content)
    url_list = selector.css("h2 a::attr(href)").getall()

    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(text=html_content)
    next_url = selector.css("a.next ::attr(href)").get()

    return next_url


# Requisito 4
def scrape_news(html_content):
    selector = parsel.Selector(text=html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1::text").get()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    reading_time = selector.css(".meta-reading-time::text").get()
    summary = selector.css(".entry-content p").get()
    category = selector.css(".meta-category span.label::text").get()

    data = {
        "url": url,
        "title": title.strip("\xa0"),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time.split(" ")[0]),
        "summary": re.sub("<.*?>", "", summary).strip(),
        "category": category,
        }
    return data


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    pages = []
    result = []

    while len(pages) < amount:
        page_content = fetch(url)
        pages.extend(scrape_updates(page_content))
        url = scrape_next_page_link(page_content)

    for url in pages[: amount]:
        page = fetch(url)
        page_data = scrape_news(page)
        result.append(page_data)

    create_news(result)

    return result
