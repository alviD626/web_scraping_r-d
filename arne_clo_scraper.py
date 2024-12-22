from functools import partial
import re

from bs4 import BeautifulSoup
from pydantic import HttpUrl

from decorators import handle_scraping_errors
from models.data import Product
from models.mapping import _get_mapped_product
from scraping.request import get_source_by_requests
from utils import extract_number


BRAND = "Arne clo"
BASE_URL = "https://arneclo.com/en-us"


def extract_product_urls(category_url: str) -> list[str]:
    """Extract product URLs from a category page"""
    all_urls = []
    source = get_source_by_requests(category_url)
    find_pagination = source.find("div",id="product-grid").find("div",class_="pagination text-center")
    # print(find_pagination)
    if find_pagination is None:
        find_product_urls = source.find("div",class_="collection_template").find("div",id="product-grid").find("div", class_="arne-collection-products").find_all("div",class_="arne-product-card-container")
        for product_url in find_product_urls:
            new_url = product_url.find("a")["href"]
            all_urls.append(f"https://arneclo.com{new_url}")
        # print(len(set(all_urls)))
        # print(len(all_urls))
        return all_urls
    else:
        pages = int(find_pagination.find_all("span",class_="page")[-1].get_text(strip = True))
        for page_no in range(1,pages+1):
            new_url = f"{category_url}?page={page_no}"
            source = get_source_by_requests(new_url)
            find_product_urls = source.find("div",class_="collection_template").find("div",id="product-grid").find("div", class_="arne-collection-products").find_all("div",class_="arne-product-card-container")
            for product_url in find_product_urls:
                new_url = product_url.find("a")["href"]
                all_urls.append(f"https://arneclo.com{new_url}")
        # print(len(set(all_urls)))
        # print(len(all_urls))
        return all_urls



handle_scraping_errors = partial(handle_scraping_errors, model=Product, prefix="get_")


@handle_scraping_errors()
def get_pid(product_url: str) -> str:
    """Extract product ID from URL"""
    return product_url.split('products/')[-1]


@handle_scraping_errors()
def get_name(source: BeautifulSoup) -> str:
    """Extract product name"""
    name_element = source.find('h1', class_='product-single__title')
    return name_element.get_text(strip=True).split('-')[0].strip()


@handle_scraping_errors()
def get_currency(source: BeautifulSoup) -> str:
    """Extract currency symbol"""
    price_element = source.find('span', {'id': 'ProductPrice'})
    return price_element.get_text(strip=True)[0]


@handle_scraping_errors()
def get_price(source: BeautifulSoup) -> float:
    """Extract price"""
    price_element = source.find('span', {'id': 'ProductPrice'})
    return float(price_element.get_text(strip=True).replace('$', '').strip())


@handle_scraping_errors()
def get_color_name(source: BeautifulSoup) -> str:
    """Extract color name"""
    color_element = source.find('span', class_='product-single__prices')
    return color_element.get_text(strip=True)


@handle_scraping_errors()
def get_colors(source: BeautifulSoup) -> list[str]:
    """Extract available colors"""
    colors = []
    color_swatches = source.find_all('div', class_='arne-color-swatch-element')
    for swatch in color_swatches:
        if swatch.find('a'):  # Only if it has a link (available color)
            colors.append(swatch.find('a')['href'].split('-')[-1])
    return colors


@handle_scraping_errors()
def get_sizes(source: BeautifulSoup) -> list[str]:
    """Extract available sizes"""
    sizes = []
    size_elements = source.find("div", class_="swatch clearfix option_size").find('div', class_='sizeswatch').find_all('div', class_='swatch-element')
    for size in size_elements:
        sizes.append(size['data-value'])
    return sizes


@handle_scraping_errors()
def get_description(source: BeautifulSoup) -> str:
    """Extract product description"""
    model_info = source.find('div', class_='accordions-content')
    if model_info:
        return model_info.get_text(strip=True)
    return None


@handle_scraping_errors()
def get_compositions(source: BeautifulSoup) -> list[str]:
    """Extract material compositions"""
    # Find content div with class 'content b'
    content_div = source.find('div', class_='content b')
    if content_div:
        # Find all li elements
        li_elements = content_div.find_all('li')
        
        # Look for first li tag containing percentage symbol
        for li in li_elements:
            text = li.get_text(strip=True)
            if '%' in text:
                compositions = []
                
                # If multiple percentages exist
                if text.count('%') > 1:
                    # Initialize variables for building composition parts
                    current_percentage = ''
                    current_material = ''
                    parts = text.split()
                    
                    # Iterate through each word
                    for i, part in enumerate(parts):
                        if '%' in part:
                            # Found a percentage
                            current_percentage = part
                            # Get the material that follows the percentage
                            if i + 1 < len(parts):
                                current_material = parts[i + 1]
                                # Add complete composition to list
                                compositions.append(f"{current_percentage} {current_material}")
                    return compositions
                else:
                    # Single composition case
                    return [text]
                
    return []


@handle_scraping_errors()
def get_all_image_urls(source: BeautifulSoup) -> list[str]:
    """Extract all product image URLs"""
    image_urls = []
    image_containers = source.find_all('div', class_='image-container')
    for container in image_containers:
        img = container.find('img')
        if img and img.get('data-src'):
            image_url = img['data-src']
            if not image_url.startswith('http'):
                image_url = f"https:{image_url}"
            image_urls.append(image_url)
    return list(set(image_urls))


@handle_scraping_errors()
def get_image_url(source: BeautifulSoup) -> str:
    """Extract main product image URL"""
    first_image = source.find('div', class_='image-container').find('img')
    if first_image and first_image.get('data-src'):
        image_url = first_image['data-src']
        if not image_url.startswith('http'):
            image_url = f"https:{image_url}"
        return image_url


def is_product_available(source: BeautifulSoup) -> bool:
    """Check if product is available"""
    return bool(source.find('div', class_='sizeswatch'))


def parse_product_data(
    product_url: str, category_metadata: dict, source: BeautifulSoup
) -> Product:
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