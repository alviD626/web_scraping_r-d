from functools import partial

from bs4 import BeautifulSoup
from pydantic import HttpUrl

from decorators import handle_scraping_errors
from logger import logger
from models.data import Product
from models.mapping import _get_mapped_product
from scraping.request import get_source_by_requests
from utils import extract_number


BRAND = "<brand_name"
BASE_URL = "<brand_url>"


def extract_product_urls(category_url: str) -> list[str]:
    ...


handle_scraping_errors = partial(handle_scraping_errors, model=Product, prefix="get_")


@handle_scraping_errors()
def get_pid(product_url: str) -> str:
    ### code here


@handle_scraping_errors()
def get_name(source: BeautifulSoup) -> str:
    ### code here


@handle_scraping_errors()
def get_currency(source: BeautifulSoup) -> str:
    ### code here


@handle_scraping_errors()
def get_price(source: BeautifulSoup) -> str:
    ### code here


@handle_scraping_errors()
def get_discount_percentage(source: BeautifulSoup) -> str:
    ### code here


@handle_scraping_errors()
def get_price_after_discount(source: BeautifulSoup) -> str:
    ### code here

@handle_scraping_errors()
def get_color_name(source: BeautifulSoup) -> str:
    ### code here


@handle_scraping_errors()
def get_colors(source: BeautifulSoup) -> list[str]:
    ### code here


@handle_scraping_errors()
def get_sizes(source: BeautifulSoup) -> list[str]:
    ### code here


@handle_scraping_errors()
def get_rating(source: BeautifulSoup) -> str:
    ### code here


@handle_scraping_errors()
def get_review_count(source: BeautifulSoup) -> str:
    ### code here


@handle_scraping_errors()
def get_description(source: BeautifulSoup) -> str:
    ### code here


@handle_scraping_errors()
def get_compositions(source: BeautifulSoup) -> list[str]:
    ### code here


@handle_scraping_errors()
def get_all_image_urls(source: BeautifulSoup) -> list[str]:
    ### code here


@handle_scraping_errors()
def get_image_url(source: BeautifulSoup) -> str:
    ### code here


@handle_scraping_errors()
def get_manufacturing_country(source: BeautifulSoup) -> str:
    ### code here


def is_product_available(source: BeautifulSoup) -> bool:
    return True


def parse_product_data(
    product_url: str, category_metadata: dict, source: BeautifulSoup
) -> Product:
    product = Product(
        brand=BRAND,
        product_url=HttpUrl(product_url),
        region=category_metadata["region"],
        market=category_metadata["market"],
        category=category_metadata["category"],
        start_date=category_metadata["start_date"],
        pid=get_pid(product_url),
        name=get_name(source),
        ### Add the rest of the attributes
    )

    return product


async def scrape_product(product_url: str, category_metadata: dict) -> Product:
    source = get_source_by_requests(product_url)
    if is_product_available(source):
        return parse_product_data(product_url, category_metadata, source)


def parse_compositions(compositions: list[str]) -> list[tuple[str, float]]:
    parsed = []
    try:
        # Iterate over all the components
        for composition in compositions:
            # Split string (format: "<percentage>% <material>")
            percentage, material = composition.split("% ")
            # Enforce data types
            parsed.append((material.strip(), extract_number(percentage.strip())))
    except Exception:
        pass

    # Sort the compositions dictionary based on percentage in descending order
    parsed = sorted(parsed, key=lambda item: item[1], reverse=True)
    return parsed


get_mapped_product = partial(_get_mapped_product, parse_compositions=parse_compositions)
