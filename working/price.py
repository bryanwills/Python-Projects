import requests
from bs4 import BeautifulSoup
import smtplib
import time
import datetime
import urllib3

url = 'https://www.amazon.com/RAVPower-Portable-26800mAh-Recharged-Nintendo/dp/B01LRQDAEI/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=mbpslow-20&linkId=ab82ae5d13e3aafdea80e6f63cb3f4ec&language=en_US'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

response = requests.get(url, headers=headers)

# print(response.text)
soup = BeautifulSoup(response.content, features="lxml")
# title = soup.select("#productTitle")[0].get_text().strip()
title = soup.find('span', id='productTitle').get_text().strip()
# print(title)


def check_price():

    price = soup.find(
        'span', id="priceblock_ourprice").get_text()  # .strip("$")
    new_price = float(price[1:6])
    # print(new_price)
#converted_price = float(price)
    if(new_price < 60.00):
        send_mail()
    print(new_price)
    print(title.strip())
    if(new_price < 59.99):
        send_mail()


url = 'https://www.amazon.com/RAVPower-Portable-26800mAh-Recharged-Nintendo/dp/B01LRQDAEI/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=mbpslow-20&linkId=ab82ae5d13e3aafdea80e6f63cb3f4ec&language=en_US'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

response = requests.get(url, headers=headers)

# print(response.text)
soup = BeautifulSoup(response.content, features="lxml")
# title = soup.select("#productTitle")[0].get_text().strip()
title = soup.find('span', id='productTitle').get_text().strip()
# print(title)


def check_price():

    price = soup.find(
        'span', id="priceblock_ourprice").get_text()  # .strip("$")
    new_price = float(price[1:6])
    # print(new_price)
#converted_price = float(price)
    if(new_price < 60.00):
        send_mail()
    print(new_price)
    print(title.strip())
    if(new_price < 59.99):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('bryanwi09@gmail.com', 'avkutwfvjrjizdzh')

    subject = 'Item is on sale!'
    body = 'check Amazon link https://www.amazon.com/RAVPower-Portable-26800mAh-Recharged-Nintendo/dp/B01LRQDAEI/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=mbpslow-20&linkId=ab82ae5d13e3aafdea80e6f63cb3f4ec&language=en_US'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'bryanwi09@gmail.com',
        'engbryanwills@gmail.com',
        msg
    )
    print('EMAIL HAS BEEN SENT!')

    server.quit()


while(True):
    check_price()
    time.sleep(60)
