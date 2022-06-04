import requests
import os
import smtplib
from bs4 import BeautifulSoup

# set the price threshold for the product
PRICE_THRESHOLD = 70

# grab the URL and headers
URL = "https://www.amazon.com/Anker-Portable-PowerCore-Essential-Compatible/dp/B08LG2X98F/ref=psdc_7073959011_t2_B0899Z4YPZ"
headers = {
    'User-Agent': 'Chrome/102.0.5005.63',
    'Accept-Language': 'en-US,en;q=0.9'
}

# set email and pass for sending email later
my_email = os.environ['email']
password = os.environ['password']

# scrape the webpage for the product name and cost (product name limited to 30 characters)
response = requests.get(URL, headers=headers)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
price = float(soup.find(class_='a-offscreen').get_text().strip('$'))
product = soup.find(id='productTitle').get_text().strip()[:30]

# if the price is below the threshold, send the email
if price < PRICE_THRESHOLD:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='joey.ohannesian@yahoo.com',
            msg=f'Subject:Price Alert - {product}\n\n'
                f'Great news! The {product} has gone below your price threshold of ${PRICE_THRESHOLD}.\n'
                f'Here is a direct link: {URL}.'
        )
