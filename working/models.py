from pexels_api import API

PEXELS_API_KEY = '563492ad6f91700001000001de8ec7b23dc3431798ac1d6b9d945791'

api = API(PEXELS_API_KEY)

api.search('models', page=1, results_per_page=20)
photos = api.get_entries()

for photo in photos:
    print('Photographer: ', photo.photographer)
    print('Photo url: ', photo.url)
    print('Photo original size: ', photo.original)



