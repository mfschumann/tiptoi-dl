import json
import logging
import re
import sys
import time
from pathlib import Path

import coloredlogs
import requests
from bs4 import BeautifulSoup

BASEPATH = Path(__file__).resolve().parents[2]

LOGGER = logging.getLogger("TipToiCatalog")
LOGGER.addHandler(logging.StreamHandler(sys.stdout))
coloredlogs.install(level="INFO", logger=LOGGER)


class TipToiCatalog:
    def __init__(self, target: str = ""):
        self.base_url = (
            "https://service.ravensburger.de/tiptoi%C2%AE/tiptoi%C2%AE_Audiodateien"
        )
        self.catalog = []
        self.products = []
        LOGGER.info("Start data scraping")
        self.get_catalog(target)
        for product in self.catalog:
            self.products.append(self.get_product_data(product))
            time.sleep(0.1)
        self.persist_products()

    def get_catalog(self, target):
        r = requests.get(self.base_url, timeout=10)
        LOGGER.info(f"Status code: {r.status_code}")
        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.find_all("a", class_="mt-listing-detailed-subpage-title")
        LOGGER.info(f"Found {len(links)} links")
        for link in links:
            if target:
                if target in link.get("title"):
                    self.catalog.append(
                        {"title": link.get("title"), "url": link.get("href")}
                    )
            else:
                self.catalog.append(
                    {"title": link.get("title"), "url": link.get("href")}
                )

    def sanitize_title(self, product: dict) -> dict:
        product["title"] = re.sub(r"\s\d{5}.*$", "", product["title"])
        product["title"] = product["title"].replace("tiptoi®", "")
        product["title"] = product["title"].replace(
            "Audiodatei", ""
        )  # ravensburger typo *shrug*
        product["title"] = product["title"].replace(
            "Audioatei", ""
        )  # ravensburger typo *shrug*
        product["title"] = product["title"].replace("\xa0", " ")
        product["title"] = product["title"].strip()
        return product

    def get_product_numbers(self, product: dict) -> dict:
        numbers = re.findall(r"\d{5}", product["title"])

        product["numbers"] = numbers
        return product

    def get_product_image(self, img: str | None) -> str:
        if img:
            url = img.split("?")[0]
            return url
        return ""

    def get_product_data(self, product: dict) -> dict:
        product = self.get_product_numbers(product)
        product = self.sanitize_title(product)
        LOGGER.info(f"Get product data for {product['title']}")
        product_data = {}

        r = requests.get(product["url"], timeout=10)
        LOGGER.info(f"Status code: {r.status_code}")

        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.find_all(
            "a",
            href=re.compile(r"\.gme"),
        )

        for n, link in enumerate(links):
            product_data["gme"] = link.get("href")
            product_data["title"] = product["title"]
            product_data["number"] = ""
            if product["numbers"]:
                try:
                    product_data["number"] = product["numbers"][n]
                except IndexError:
                    LOGGER.warning(
                        "Inconsitent data for %s, catalog maybe not 100%% complete",
                        product_data["title"],
                    )
            if link.img:
                product_data["img"] = self.get_product_image(link.img.get("src"))
        return product_data

    def persist_products(self):
        LOGGER.info("Write json file")
        (BASEPATH / "output").mkdir(exist_ok=True)
        with open(BASEPATH / "output/products.json", "w") as f:
            json.dump(self.products, f)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        ttc = TipToiCatalog(sys.argv[1])
    ttc = TipToiCatalog()
