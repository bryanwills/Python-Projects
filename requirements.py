import requests
from bs4 import BeautifulSoup

#url = raw_input("https://www.imdb.com/movies-coming-soon/")

page = requests.get('https://www.imdb.com/movies-coming-soon/')
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)