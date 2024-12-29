import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASEPATH = Path(__file__).resolve().parents[2]


class TipToiCatalog:
    def __init__(self):
        self.base_url = (
            "https://service.ravensburger.de/tiptoi%C2%AE/tiptoi%C2%AE_Audiodateien"
        )
        self.catalog = []
        self.products = []
        self.get_catalog()
        for product in self.products:
            self.products.append(self.get_product_data(product))
        self.persist_products()

    def get_catalog(self):
        r = requests.get(self.base_url)
        print(f"Status code: {r.status_code}")
        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.find_all("a", class_="mt-listing-detailed-subpage-title")
        print("Found {len(links)} links")
        for link in links:
            self.catalog.append({"title": link.get("title"), "url": link.get("href")})

    def sanitize_title(self, product: dict) -> dict:
        product["title"] = re.sub(r"\s\d{5}.*$", "", product["title"])
        product["title"] = product["title"].replace("tiptoi® Audiodatei ", "")
        product["title"] = product["title"].replace(
            "tiptoi® Audioatei ", ""
        )  # ravensburger typo *shrug*
        product["title"] = product["title"].replace("\xa0", " ")
        return product

    def get_product_numbers(self, product: dict) -> dict:
        numbers = re.findall(r"\d{5}", product["title"])
        product["numbers"] = numbers
        return product

    def get_product_image(self, img: str) -> str:
        url = img.split("?")[0]
        return url

    def get_product_data(self, product: dict) -> dict:
        product = self.get_product_numbers(product)
        product = self.sanitize_title(product)
        print(f"Get product data for {product['title']}")
        product_data = {}

        r = requests.get(product["url"])

        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.find_all(
            "a",
            href=re.compile(r"\.gme"),
        )
        for n, link in enumerate(links):
            product_data["gme"] = link.get("href")
            product_data["title"] = product["title"]
            product_data["number"] = product["numbers"][n]
            if link.img:
                product_data["img"] = self.get_product_image(link.img.get("src"))
        return product_data

    def persist_products(self):
        print("Write json file")
        with open(BASEPATH / "products.json", "w") as f:
            json.dump(self.products, f)


if __name__ == "__main__":
    ttc = TipToiCatalog()
