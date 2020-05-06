import requests
import shutil
from bs4 import BeautifulSoup

def get_html(url):
	r = requests.get(url)
	if not r.ok:
		print('Oops')
	return r.text

def scrape_photos_links(html):
	soup = BeautifulSoup(html, 'lxml')
	photos_items = soup.find_all('img', class_='photo-item__img')
	print(photos_items)


def download_file(url):
	filename = url.split('/')[-1]
	r = requests.get(url, stream=True)
	if r.ok:
		with open('file.jpeg', 'wb') as file:
			for chunk in r.iter_content(1024 * 100):
				file.write(chunk)
	else:
		print('Oops!')

def download_file2(url):
	filename = url.split('/')[-1]
	with requests.get(url, stream=True) as r:
		with open(filename, 'wb') as file:
			shutil.copyfileobj(r.raw, file)

def main():
	url = 'https://www.pexels.com/search/landscape/'
	scrape_photos_links(get_html(url))


if __name__ == '__main__':
	main()
