import requests
THE_URL = 'https://www.whitehouse.gov/briefing-room/press-briefings?page='
MAX_PAGE_NUM = 162
for pagenum in range(0, MAX_PAGE_NUM):
    url = THE_URL + str(pagenum)
    print("Downloading", url)
    resp = requests.get(url)

    fname = str(pagenum) + '.html'
    print("Saving to", fname)
    with open(fname, "w") as wf:
        wf.write(resp.text)
