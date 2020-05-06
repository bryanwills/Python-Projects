import requests
import bs4 as BeautifulSoup


def download_file(url):
	filename = url.split('/')[-1]
	r = requests.get(url, stream=True)
	if r.ok:
		with open('file.jpeg', 'wb') as file:
			for chunk in r.iter_content(1024 * 100):
				file.write(chunk)
	else:
		print('Oops!')

def main():
	url = 'https://images.pexels.com/photos/414171/pexels-photo-414171.jpeg'
	download_file(url)


if __name__ == '__main__':
	main()