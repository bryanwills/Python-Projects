import requests
from bs4 import BeautifulSoup as soup

DOMAIN = 'http://purehumbug.com'
URL = 'http://purehumbug.com/shows/2006/1-99/'
FILETYPE = '.mp3'


def get_soup(url):
    return soup(requests.get(url).text, 'html.parser')


for link in get_soup(URL).find_all('a'):
    file_link = link.get('href')
    if FILETYPE in file_link:
        print(file_link)
        with open(link.text, 'wb') as file:
            response = requests.get(DOMAIN + file_link)
            file.write(response.content)
