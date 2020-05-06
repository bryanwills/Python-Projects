# coding: utf-8
# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

# specify the url
url = "http://172.21.1.230"

# Connect to the website and return the html to the variable ‘page’
try:
    page = urlopen(url)
except:
    print("Error opening the URL")

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
#content = soup.find('div', {"class": "float-l"})
content = soup.find('div', class_='tonerArea').find('title').text.strip()

article = ''
for i in content.findAll('p'):
    article = article + ' ' +  i.text
print(article)

# Saving the scraped text
with open('scraped_text.txt', 'w') as file:
    file.write(article)


 #def get_detail_data(soup):
	#title price, items sold
#	try:
#		title = soup.find('h1', id='itemTitle').text
#	except:
#		title = ''
#
#	try:
#		try:
#			p = soup.find('span', id='prcIsum').text.strip()
#		except:
#			p = soup.find('span', id='mm-saleDscPrc').text.strip()
#		currency, price = p.split(' ')
#	except:
#		currency = ''
#		price = ''
#
#	try:
#		sold = soup.find('span', class_='vi-qtyS-hot-red').find('a').text.strip().split(' ')[0].replace('\xa0', '')
#	except:
#		sold = ''
#
#	data = {
#
#		'title': title,
#		'price': price,
#		'currency': currency,
#		'total sold': sold
#	}
#	return data
