import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
 
 
baseurl = requests.get('https://www.usa.gov/federal-agencies/')
valid_pages = 'abcdefghijlmnoprstuvw'
for n in range(len(valid_pages)):
        url = f'{baseurl}{valid_pages[n]}'
        print(url)
        page = soup = BeautifulSoup(url, 'html.parser')
        
        for page in soup.find_all('ul', {'class' : 'one_column_bullet'}):
         
         
                print(page)
