import requests
from bs4 import BeautifulSoup
import logging

fmt = "%(asctime)s [%(levelname)s]: %(message)s"
logging.basicConfig(level=logging.INFO, format=fmt)

url = "https://www.nike.com/cz/w/muzi-obuv-nik1zy7ok"
logging.info("Scraping: ")
r = requests.get(url)
logging.info("DONE")

if r.status_code != 200:
    logging.warning("NEUSPESNY SCRAPE")

soup = BeautifulSoup(r.text, "html.parser")
soup = soup.find("main")
products = soup.find_all("div", {"class": "product-card product-grid__card css-c2ovjx"})

products_parsed = []

for product in products:

    print(product)

    name = product.find("div", "product-card__title").text
    price_before = product.find("div", {"class": ["product-price", "cz__styling", "is--striked-out", "css-0"]})
    price_after = product.find("div", "product-price is--current-price css-1ydfahe")
# nadpis = inzerat.find("h2", {"class": "nadpis"})
# url = inzerat.find("a")['href']
# nadpis = nadpis.find("a").text.strip()

#     cena = inzerat.find("div", {"class": "inzeratycena"}).find("b").text.strip()
#     zobrazeni = inzerat.find("div", {"class": "inzeratyview"}).text.strip('x').strip()
#     lokalita = inzerat.find("div", {"class": "inzeratylok"}).text.split("<br>")
#     mesto = lokalita[0].strip()
#     # psc = lokalita[1].strip()
#     datum_pridani = inzerat.find("span", {"class": "velikost10"}).text.strip()
#dsf
    products_parsed.append({
        "name": name,
        "price before": price_before,
        "price after": price_after

    })
#
    print(products_parsed)
#
#     r2 = requests.get(url)


logging.debug("END")
