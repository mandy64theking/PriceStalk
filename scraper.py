import requests
from bs4 import BeautifulSoup
import smtplib

URL = input("Enter URL :")
budget = float(input("Enter Alert Amount :"))

headers = {
    "User-Agent":
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.16 Safari/537.36 Edg/80.0.361.9'
}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    try:
        price = soup.find(id="priceblock_dealprice").get_text()
        # Sometimes Amazon uses deal price for special deals
    except:
        price = soup.find(id="priceblock_ourprice").get_text()
    # TODO Fix issues with deal price/our price
    converted_price = float(price[2:4] + price[5:8])
    if (converted_price < budget):
        send_mail()
    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('scraperamazonflipkart@gmail.com', 'hdbuscxtxxsqyuvh')

    subject = 'Price fell down! DO NOT REPLY.This is a System-genrated mail'
    body = 'Check the amazon Link ' + URL

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail('scraperamazonflipkart@gmail.com',
                    'mandy64theking@gmail.com', msg)
    print("Email has been sent")
    server.quit()


check_price()
