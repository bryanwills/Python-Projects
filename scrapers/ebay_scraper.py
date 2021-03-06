# TODO
from bs4 import BeautifulSoup
import requests
import csv


def get_page(url):
	response = requests.get(url)
	#print(response.ok)
	#print(response.status_code)

	if not response.ok:
		print('Server responded:', response.status_code)
	else:
		soup = BeautifulSoup(response.text, 'lxml')
	return soup


def get_detail_data(soup):
	#title price, items sold
	try:
		title = soup.find('h1', id='itemTitle').text
	except:
		title = ''

	try:
		try: 
			p = soup.find('span', id='prcIsum').text.strip()
		except:
			p = soup.find('span', id='mm-saleDscPrc').text.strip()
		currency, price = p.split(' ')
	except:
		currency = ''
		price = ''

	try:
		sold = soup.find('span', class_='vi-qtyS-hot-red').find('a').text.strip().split(' ')[0].replace('\xa0', '')
	except:
		sold = ''

	data = {

		'title': title,
		'price': price,
		'currency': currency,
		'total sold': sold
	}
	return data 

def get_index_data(soup):

	try:
		links = soup.findAll('a', class_='s-item__link')
	except:
		links = []

	urls = [item.get('href') for item in links]
	
	return urls


def write_csv(data, url):
	with open('outputebay.csv', 'a') as csvfile: #appended data to csv
		writer = csv.writer(csvfile)

		row = [data['title'], data['price'], data['currency'], data['total sold'], url]

		writer.writerow(row)


	#print(title)
	#print(price)
	#print(currency)
	#print(sold)

def main():
	url ='https://www.imdb.com/movies-coming-soon/'

	products = get_index_data(get_page(url))

	for link in products:
		data = get_detail_data(get_page(link))
		write_csv(data, link)


if __name__ == '__main__':
	main()