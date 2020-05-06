import requests
import shutil


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
	url = 'https://images.pexels.com/photos/414171/pexels-photo-414171.jpeg'
	download_file(url)
	download_file2(url)


if __name__ == '__main__':
	main()