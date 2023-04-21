from bs4 import BeautifulSoup
import requests


def parse_jokes(url_jokes):
    page = requests.get(url_jokes)

    filtered_news = []

    soup = BeautifulSoup(page.text, "html.parser")

    all_news = soup.findAll('div', class_='anekdot')

    for data in all_news:
        filtered_news.append((data.text, 0, 0, 0))

    return filtered_news
