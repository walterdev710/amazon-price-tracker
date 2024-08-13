import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

USER_NAME = "user name"
USER_PASS = "user password"

PRODUCT_URL = "https://www.amazon.com/YSSOA-Gaming-Office-Adjustable-Chair/dp/B08XQNSH7B/ref=sr_1_6?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&dib=eyJ2IjoiMSJ9.V8UTj_BM6DBuzJSqQ0WnPOOjp0lD7u1B3gbyC3B9UjHe-NwYtOSp8AXDzW7Oz1LmSjZ9iknYxk8PSlkh7KxKRjFuua47kQxG-jWuX2IFFg2q430yjxqdtA0Hs0NgxDZLIS1UmPd9w9W7ThJzA0sk9fGS9TZeIjrDpyGXxEiubYXOfejBlvaT2xHGgkGbMQXn5WP2FgS1Z2Op83Hmub_1V73q4ZLIlneQFcjMzY41Mbot4xEceta4sLYQh6pML35ukBJvLsn4AntlBiJo_nNfxT338fSX4RytDxr6DSIo6LQ.YnJI596MXVn1ayVzm7RupwACW9bcu6ViFxw_0pN2ZWI&dib_tag=se&keywords=gaming+chairs&pd_rd_r=add7208a-5774-42d0-b128-fef6161513c8&pd_rd_w=EVjyj&pd_rd_wg=idk0D&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=A5GG4562T4AB20ZGHTGG&qid=1723560103&sr=8-6"

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Accept-Language":"en-US,en;q=0.5"
}

response = requests.get(url=PRODUCT_URL, headers=headers)
amazon_product_webpage = response.text

soup = BeautifulSoup(amazon_product_webpage, "lxml")
whole_price = soup.find(name="span", class_="a-price-whole").get_text()
fraction_price = soup.find(name="span", class_="a-price-fraction").get_text()
float_price = float(f"{whole_price}.{fraction_price}")
product_title = soup.find(name="span", id="productTitle").getText()

if float_price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=465) as connection:
        connection.starttls()
        connection.login(user=USER_NAME, password=USER_PASS)
        connection.sendmail(from_addr=USER_NAME, to_addrs=USER_NAME, msg=f"Subject:Amazon Price Alert\n\n{product_title.strip()} is now ${float_price}\n{PRODUCT_URL}")

