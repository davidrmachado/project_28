import requests
import time
import parsel


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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
