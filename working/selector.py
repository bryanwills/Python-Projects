from selectorlib import Extractor
import requests
import json
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('url', help='Amazon Product Details URL')

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('selectors.yml')

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
headers = {'User-Agent': user_agent}

# Download the page using requests
args = argparser.parse_args()
r = requests.get(args.url, headers=headers)
# Pass the HTML of the page and create
data = e.extract(r.text)
# Print the data
print(json.dumps(data, indent=True))
