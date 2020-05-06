#!/usr/bin/python3
import urllib.request
import sys


def tiny_url(url):
    apiurl = "https://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")


url = sys.argv[1]
print(url)
print(tiny_url(url))
