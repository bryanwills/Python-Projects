from bs4 import BeautifulSoup
import requests

url = "https://boston.craigslist.org/search/sof"

# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'lxml')

# Extracting all the <a> tags whose class name is 'result-title' into a list.
titles = soup.findAll('a', {'class': 'result-title'})

# Extracting text from the the <a> tags, i.e. class titles.
for title in titles:
    print(title.text)
