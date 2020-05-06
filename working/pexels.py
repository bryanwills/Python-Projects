# model scraping for themodelbot

import requests
from bs4 import BeautifulSoup as bs
import os
from pexels_api import API

PEXELS_API_KEY = '563492ad6f91700001000001de8ec7b23dc3431798ac1d6b9d945791'

api = API(PEXELS_API_KEY)
# website with model images
url = 'https://api.pexels.com/v1/search?query=models&per_page=15&page=1'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for model images
if not os.path.exists('models'):
    os.makedirs('models')

# move to new directory
os.chdir('models')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass



api.search('models', page=1, results_per_page=20)
photos = api.get_entries()

for photo in photos:
    print('Photographer: ', photo.photographer)
    print('Photo url: ', photo.url)
    print('Photo original size: ', photo.original)






