from bs4 import BeautifulSoup
import requests

url_jokes = "http://anekdotov.net/anekdot/"
page = requests.get(url_jokes)

filtered_news = []
all_news = []

soup = BeautifulSoup(page.text, "html.parser")

all_news = soup.findAll('div', class_='anekdot')

for data in all_news:
    filtered_news.append(data.text)

print(filtered_news)

# print(soup)

