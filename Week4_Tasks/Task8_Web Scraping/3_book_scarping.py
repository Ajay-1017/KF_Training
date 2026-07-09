import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

source = requests.get(url).text
# print(source)

soup = BeautifulSoup(source,'lxml')
