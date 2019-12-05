from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.bbc.com/news/world-europe-50653597").text

soup = BeautifulSoup(source, "lxml")
soup2 = BeautifulSoup(source, "html.parser")
print(soup.prettify())
print(soup2.prettify())