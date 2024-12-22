from functools import partial
import re

from bs4 import BeautifulSoup
from pydantic import HttpUrl

from decorators import handle_scraping_errors
from models.data import Product
from models.mapping import _get_mapped_product
from scraping.request import get_source_by_requests
from utils import extract_number


BRAND = "Muji"
BASE_URL = "https://www.muji.us"


def extract_product_urls(category_url: str) -> list[str]:
    """Extract product URLs from a category page"""
    all_urls = []
    source = get_source_by_requests(category_url)
    find_pagination = source.find("div",class_="collection-page-product-grid").find("div",class_="productgrid--wrapper").find("nav",class_="pagination--container")
    if find_pagination is None:
        find_product_urls = source.find("div",class_="collection-page-product-grid").find("div",class_="productgrid--wrapper").find("ul").find_all("li")
        for product_url in find_product_urls:
            new_url = product_url["data-product-quickshop-url"]
            all_urls.append(f"https://www.muji.us{new_url}")
        # print(len(set(all_urls)))
        # print(len(all_urls))
        return all_urls
    else:
        pages = int(find_pagination.find("ul").find_all("li")[-2].get_text(strip = True))
        for page_no in range(1,pages+1):
            new_url = f"{category_url}?page={page_no}"
            source = get_source_by_requests(new_url)
            find_product_urls = source.find("div",class_="collection-page-product-grid").find("div",class_="productgrid--wrapper").find("ul").find_all("li")
            for product_url in find_product_urls:
                new_url = product_url["data-product-quickshop-url"]
                all_urls.append(f"https://www.muji.us{new_url}")
        # print(len(set(all_urls)))
        # print(len(all_urls))
        return all_urls
    # print(find_pagination)


handle_scraping_errors = partial(handle_scraping_errors, model=Product, prefix="get_")


@handle_scraping_errors()
def get_pid(product_url: BeautifulSoup) -> str:
    """Extract product ID"""
    return product_url.split('/')[-1].split("-")[-1]


@handle_scraping_errors()
def get_name(source: BeautifulSoup) -> str:
    """Extract product name"""
    name_element = source.find('h1', class_='product-title')
    return name_element.get_text(strip=True)


@handle_scraping_errors()
def get_currency(source: BeautifulSoup) -> str:
    """Extract currency symbol"""
    price_element = source.find("div",class_="price__current").find("span",class_="money")
    return price_element.get_text(strip=True)[0]


@handle_scraping_errors()
def get_price(source: BeautifulSoup) -> float:
    """Extract price"""
    price_element = source.find("div",class_="price__current").find("span",class_="money")
    price_text = price_element.get_text(strip=True).replace('$', '')
    return price_text


@handle_scraping_errors()
def get_color_name(source: BeautifulSoup) -> str:
    """Extract color name"""
    color_element = source.find('div', class_="product-form--regular").find("variant-selection",class_="variant-selection").find("legend",class_="options-selection__option-header").get_text(strip=True).split(":")[-1]
    return color_element


@handle_scraping_errors()
def get_colors(source: BeautifulSoup) -> list[str]:
    """Extract available colors"""
    colors_elements = source.find('div', class_="product-form--regular").find("variant-selection",class_="variant-selection").find("div",class_="options-selection__option-values").find_all("label",class_="options-selection__option-value-label")
    colors = []
    for element in colors_elements:
        new_colors = element.find("input")["value"]
        colors.append(new_colors)
    return list(set(colors))


@handle_scraping_errors()
def get_sizes(source: BeautifulSoup) -> list[str]:
    """Extract available sizes"""
    size_elements = source.find_all('span', {'class': 'options-selection__option-value-name'})
    sizes = [size.get_text(strip=True) for size in size_elements if size.get_text(strip=True)]
    return sizes


@handle_scraping_errors()
def get_description(source: BeautifulSoup) -> str:
    """Extract product description"""
    description_element = source.find('div', class_='product-description').find_all("p")[0].find("span")
    if description_element:
        return description_element.get_text(strip=True)


@handle_scraping_errors()
def get_compositions(source: BeautifulSoup) -> list[str]:
    """Extract material compositions"""
    compositions = []
    material_tab = source.find_all('div', class_='collapsible-tab__text')
    for comp in material_tab:
        if "%" in comp.get_text():
            text = comp.find("p").find("span").decode_contents().split("<br/>")[0]
            # print(text)
            # Split the text by commas and clean each part
            compositions = [item.strip() for item in text.split(":")[-1].split(',')]
            break 

    return compositions


@handle_scraping_errors()
def get_all_image_urls(source: BeautifulSoup) -> list[str]:
    """Extract all product image URLs"""
    image_urls = []
    image_elements = source.find('div', class_='product-gallery--navigation loading').find_all("img")
    for element in image_elements:
        new_images = element["src"].replace("//","").replace("org_x75","org_2000x2000")
        image_urls.append(new_images)
    return list(set(image_urls))


@handle_scraping_errors()
def get_image_url(source: BeautifulSoup) -> str:
    """Extract main product image URL"""
    first_image = source.find('div', class_='product-gallery--navigation loading').find("img")["src"].replace("//","").replace("org_x75","org_2000x2000")
    return first_image


def get_manufacturing_country(source: BeautifulSoup) -> str:
    """Extract manufacturing country"""
    details_tab = source.find('div', class_='collapsible-tab__text')
    if details_tab:
        country_text = details_tab.get_text()
        match = re.search(r'Country/Region of Origin:\s*([^*\n]+)', country_text)
        if match:
            return match.group(1).strip()


def is_product_available(source: BeautifulSoup) -> bool:
    return True


def parse_product_data(product_url: str, category_metadata: dict, source: BeautifulSoup) -> Product:
    """Parse product data into Product model"""
    product = Product(
        brand=BRAND,
        product_url=HttpUrl(product_url),
        region=category_metadata["region"],
        market=category_metadata["market"],
        category=category_metadata["category"],
        start_date=category_metadata["start_date"],
        pid=get_pid(product_url),
        name=get_name(source),
        currency=get_currency(source),
        price=get_price(source),
        color_name=get_color_name(source),
        colors=get_colors(source),
        sizes=get_sizes(source),
        description=get_description(source),
        compositions=get_compositions(source),
        manufacturing_country=get_manufacturing_country(source),
        all_image_urls=get_all_image_urls(source),
        image_url=get_image_url(source)
    )
    return product


async def scrape_product(product_url: str, category_metadata: dict) -> Product:
    """Scrape product data from URL"""
    source = get_source_by_requests(product_url)
    if is_product_available(source):
        return parse_product_data(product_url, category_metadata, source)


def parse_compositions(compositions: list[str]) -> list[tuple[str, float]]:
    """Parse material compositions into (material, percentage) tuples"""
    parsed = []
    try:
        for composition in compositions:
            percentage, material = composition.split('%')
            parsed.append((material.strip(), extract_number(percentage.strip())))
    except Exception:
        pass
    
    parsed = sorted(parsed, key=lambda item: item[1], reverse=True)
    return parsed


get_mapped_product = partial(_get_mapped_product, parse_compositions=parse_compositions)