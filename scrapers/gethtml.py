import requests
from bs4 import BeautifulSoup

#url = raw_input("https://www.imdb.com/movies-coming-soon/")

page = requests.get('https://www.imdb.com/movies-coming-soon/')
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify





	def main():
	url ='https://www.imdb.com/movies-coming-soon/'

	products = get_index_data(get_page(url))

	for link in products:
		data = get_detail_data(get_page(link))
		write_csv(data, link)


if __name__ == '__main__':
	main()