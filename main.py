import requests
from bs4 import BeautifulSoup
import smtplib
import os


URL = 'https://www.eobuwie.com.pl/buty-nike-air-max-90-qs-dj4878-400-college-navy-light-bone-sail.html?snrai_campaign=G2DJb21q2f81&snrai_id=c19829af-7d8d-4bd1-8655-f2dff20bdfab'
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
RECEIVER = os.environ.get('RECEIVER')

r = requests.get(
    url=URL,
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Accept-Language": "en-US,en;q=0.5"
    }
)
r.raise_for_status()
page = r.text

soup = BeautifulSoup(page, 'html.parser')
price = soup.find(class_='e-product-price__normal')
price = int(price.text[0:4])

if price < 400:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(USERNAME, PASSWORD)
        connection.sendmail(from_addr = USERNAME, to_addrs = RECEIVER,
                                    msg = f'Subject: Sneakers are cheaper now!!\n\nThe price of the sneakers you liked is {price} PLN now!\n '
                                        f'{URL}')