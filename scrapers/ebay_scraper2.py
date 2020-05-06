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
	url ='https://www.ebay.com/sch/i.html?_nkw=mens+watches&_pgn=1'

	products = get_index_data(get_page(url))

	for link in products:
		data = get_detail_data(get_page(link))
		write_csv(data, link)


if __name__ == '__main__':
	main		https://www.imdb.com/movies-coming-soon/


if __name__ == '__main__':
	main()


#for i in range(1, 10):     #Number of pages plus one
#       url = "http://www.pga.com/golf-courses/search?page={}&searchbox=Course+Name&searchbox_zip=ZIP&distance=50&price_range=0&course_type=both&has_events=0".format(i)
#       r = requests.get(url)
#        soup = BeautifulSoup(r.content, "html5lib")   #Can use whichever parser you prefer
# Your code for each individual page here 





