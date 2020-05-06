from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])
#print(soup.prettify()) prints all HTML code with proper indents

for article in soup.find_all('article'):
	headline = article.h2.a.text
	print(headline)

	summary = article.find('div', class_='entry-content').p.text
	print(summary)
#print(article.prettify())

#headline = article.a.text
#print(headline)

#grabs youtube URL
	try:
		vid_src = article.find('iframe', class_='youtube-player')['src']
#splits URL by forward slashes. Looking for 4th index, or 4th ' '
		vid_id = vid_src.split('/')[4]
#print(vid_id)
#saves the 0 index
		vid_id = vid_id.split('?')[0]
#print(vid_id)
#creates youtube video link by parsing data from Coreyms.com
		yt_link = f'https://youtube.com/watch?v={vid_id}'
	except Exception as e:
		yt_link = None

	print(yt_link)

	print()

	csv_writer.writerow([headline, summary, yt_link])

csv_file.close()