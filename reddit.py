import requests

def main():
	payload = {
		'op': 'login-main',
		'user': 'bryanwi09',
		'passwd': 'Wendell!917'

	}
	session = requests.session()
	session.post('https://www.reddit.com/post/login', data=payload)
	request = session.get('https://www.reddit.com/r/Python')
	print(request.headers)
	print(request.text)

if __name__ == '__main__':
	main()