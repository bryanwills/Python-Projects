import requests
from bs4 import BeautifulSoup
from flask import make_response


def getTitle(link):
    """Attempt to get a title."""
    title = ''
    if link.title.string is not None:
        title = link.title.string
    elif link.find("h1") is not None:
        title = link.find("h1")
    return title


def getDescription(link):
    """Attempt to get description."""
    description = ''
    if link.find("meta", property="og:description") is not None:
        description = link.find(
            "meta", property="og:description").get('content')
    elif link.find("p") is not None:
        description = link.find("p").content
    return description


def getImage(link):
    """Attempt to get image."""
    image = ''
    if link.find("meta", property="og:image") is not None:
        image = link.find("meta", property="og:image").get('content')
    elif link.find("img") is not None:
        image = link.find("img").get('href')
    return image


def getSiteName(link, url):
    """Attempt to get the site's base name."""
    sitename = ''
    if link.find("meta", property="og:site_name") is not None:
        sitename = link.find("meta", property="og:site_name").get('content')
    else:
        sitename = url.split('//')[1]
        name = sitename.split('/')[0]
        name = sitename.rsplit('.')[1]
        return name.capitalize()
    return sitename


def scrape(request):
    """Scrape scheduled link previews."""
    if request.method == 'POST':
        # Allows POST requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        request_json = request.get_json()
        target_url = request_json['url']
        headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        })
        r = requests.get(target_url)
        raw_html = r.content
        soup = BeautifulSoup(raw_html, 'html.parser')
        links = soup.select('.post-content p > a')
        previews = []
        for link in links:
            url = link.get('href')
            r2 = requests.get(url, headers=headers)
            link_html = r2.content
            embedded_link = BeautifulSoup(link_html, 'html.parser')
            preview_dict = {
                'title': getTitle(embedded_link),
                'description': getDescription(embedded_link),
                'image': getImage(embedded_link),
                'sitename': getSiteName(embedded_link, url),
                'url': url
            }
            previews.append(preview_dict)
        return make_response(str(previews), 200, headers)
    return make_response('bruh pls', 400, headers)
