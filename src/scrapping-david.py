from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

# Scappe URLs on product listing pages
# def make_url_list():
#     url_list = []
#     url = "https://www.oldelpaso.fr/products"
#     response = requests.get(url)
#     html = response.content
#     soup = bs(html, "lxml")
#     print(soup.find_all("div", id="product-category-results-list"))
#     return url_list

# Loop trough URLs
# for url in url_list:
url = "https://www.oldelpaso.fr/products/wraps-de-ble-nature-new"
response = requests.get(url)
html = response.content
soup = bs(html, "lxml")

product_intro = soup.find("div", class_="product-intro__text")
product_name = product_intro.h1.get_text()
# try to escape text (whitespace, linebreaks)
product_descr = product_intro.find('div', class_="product-intro__description").get_text(" ")
# make JSON
product_dict = {"name": product_name, "description": product_descr}
# Save to BDD

