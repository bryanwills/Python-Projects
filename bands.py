from bs4 import BeautifulSoup
import requests
import lxml

import pandas as pd 

#Grab users's band and sanitize it
band_name = input('Please, enter a band name:\n').strip()
formatted_band_name = band_name.replace(' ', '+')
print(f'Searching {band_name}. Wait, please...')

#Set initial URLs
base_url = 'http://www.best-cd-price.co.uk'
search_url = f'http://www.best-cd-price.co.uk/search-Keywords/1-/229816/{formatted_band_name}.html'

data = {
	'Image': [],
	'Name': [],
	'URL': [],
	'Artist': [],
	'Binding': [],
	'Format': [],
	'Release Date': [],
	'Label': [],
}

	def export_and_print(data=[]):
		table = pd.DataFrame(data, columns=[
							  'Image', 'Name', 'URL', 'Artist', 'Binding', 'Format', 'Release Date', 'Label'])
		table.index = table.index + 1
		clean_band_name = band_name.lower().replace(' ', '_')
		table.to_csv(f'{clean_band_name}'_albums.csv',
			sep=',', encoding='utf-8', index=False)
		print('Scraping done. Here are the results: ')
		print(table)