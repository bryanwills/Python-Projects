from urllib.request import urlopen
from bs4 import BeautifulSoup

file = "Details.csv"
f = open(file, "w")
Headers = "Name,Address,City,Phone,Website\n"
f.write(Headers)
for page in range(1,5):
    url = "http://www.pga.com/golf-courses/search?page={}&searchbox=Course%20Name&searchbox_zip=ZIP&distance=50&price_range=0&course_type=both&has_events=0".format(page)
    html = urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    Title = soup.find_all("div", {"class":"views-field-nothing"})
    for i in Title:
        try:
            name = i.find("div", {"class":"views-field-title"}).get_text()
            address = i.find("div", {"class":"views-field-address"}).get_text()
            city = i.find("div", {"class":"views-field-city-state-zip"}).get_text()
            phone = i.find("div", {"class":"views-field-work-phone"}).get_text()
            website = i.find("div", {"class":"views-field-website"}).get_text()
            print(name, address, city, phone, website)
            f.write("{}".format(name).replace(",","|")+ ",{}".format(address)+ ",{}".format(city).replace(",", " ")+ ",{}".format(phone) + ",{}".format(website) + "\n")
        except: AttributeError
f.close()