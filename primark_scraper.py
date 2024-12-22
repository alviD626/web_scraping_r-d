from functools import partial
import json
import time
from bs4 import BeautifulSoup
from pydantic import HttpUrl
import requests

from decorators import handle_scraping_errors
from models.data import Product
from models.mapping import _get_mapped_product
from scraping.request import get_source_by_requests
from utils import extract_number

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
}
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"


BRAND = "Primark"
BASE_URL = "https://www.primark.com"



def extract_product_urls(category_url: str) -> list[str]:
    all_urls = []
    source = get_source_by_requests(category_url)
    total_products = int(source.find("div", id = "products-top-bar").find("p", class_="MuiTypography-root MuiTypography-body2 products-top-bar-hideOnMobile css-4k385d").get_text(strip=True).split(" ")[0])
    # print(total_products)
    if total_products < 24:
        links = source.find("div", id = "products-grid").find("div", class_="MuiGrid-root MuiGrid-container css-1fg05l7").find_all("div",class_="MuiBox-root css-15dkcsy")
        for link in links:
            new_urls = link.find("a")["href"]
            all_urls.append(f"https://www.primark.com{new_urls}")
        # print(len(all_urls))
        # print(len(set(all_urls)))
        return all_urls
    else:
        total_pages = math.ceil(total_products/24)
        for i in range(1,total_pages+1):
            new_url = f"{category_url}?page={i}"
            source = get_source_by_requests(new_url)
            links = source.find("div", id = "products-grid").find("div", class_="MuiGrid-root MuiGrid-container css-1fg05l7").find_all("div",class_="MuiBox-root css-15dkcsy")
            for link in links:
                new_urls = link.find("a")["href"]
                all_urls.append(f"https://www.primark.com{new_urls}")
        # print(len(all_urls))
        # print(len(set(all_urls)))
        return all_urls
    

handle_scraping_errors = partial(handle_scraping_errors, model=Product, prefix="get_")



def get_pid(product_url: str) -> list[str]:
    id = product_url.split("/")[-1].split("-")[-1]
    return id


def get_name(source: BeautifulSoup) -> str:
    name = source.find("div",class_="HeaderAndPrice-titleWrapper MuiBox-root css-0").find("h1",class_="MuiTypography-root MuiTypography-h1Small HeaderAndPrice-productTitle css-1qylmhr").get_text(strip=True)
    return name


def get_currency(source: BeautifulSoup) -> str:
    currency = source.find("div", id = "sales-panel-wrapper-price").find("p", class_="MuiTypography-root MuiTypography-body1 HeaderAndPrice-price css-g9ki7z").get_text(strip=True)[0]
    return currency



def get_price(source: BeautifulSoup) -> str:
    price = source.find("div", id = "sales-panel-wrapper-price").find("p", class_="MuiTypography-root MuiTypography-body1 HeaderAndPrice-price css-g9ki7z").get_text(strip=True)[1:]
    return price




def get_color_name(source: BeautifulSoup) -> str:
    color = source.find("div",id = "color-selector-block-color").find("span", class_="MuiTypography-root MuiTypography-body2 css-4k385d").get_text(strip=True)
    return color



def get_colors(source: BeautifulSoup) -> list[str]:
    all_colors = []
    colors = source.find("div",id = "color-selector-block-gallery").find_all("a")
    for color in colors:
        new_colors = color["data-evergage-color"]
        all_colors.append(new_colors)
    return all_colors




def get_description(source: BeautifulSoup) -> str:
    description = source.find("div", id = "sales-panel-wrapper-header").find("h5", class_="MuiTypography-root MuiTypography-body1 HeaderAndPrice-productDescription css-g9ki7z").get_text(strip=True)
    return description



def get_details(source: BeautifulSoup) -> list[str]:
    init_details = source.find("div", id = "product-details-accordion").find("div", class_="MuiCollapse-wrapper MuiCollapse-vertical css-hboir5").find("p", class_="MuiTypography-root MuiTypography-body1 css-g9ki7z").get_text(strip=True).split("\n")
    details = [x for x in init_details if x != '']
    return details



@handle_scraping_errors()
def get_compositions(source: BeautifulSoup) -> list[str]:
    """
    Extract material composition percentages from product details.

    Args:
        source (list): List of product details strings

    Returns:
        list: List of material compositions with percentages, or empty list if no material found
    """

    init_details = source.find("div", id = "product-details-accordion").find("div", class_="MuiCollapse-wrapper MuiCollapse-vertical css-hboir5").find("p", class_="MuiTypography-root MuiTypography-body1 css-g9ki7z").get_text(strip=True).split("\n")
    details = [x for x in init_details if x != '']

    material_line = next((item for item in details if item.startswith("Material:")), None)

    if material_line:
        # Extract the material description after "Material:"
        material_description = material_line.split("Material:")[1].strip()

        # Step 1: Split at the first full stop (.) and use the first part
        first_part = material_description.split(".")[0]

        # Step 1: Extract all percentage-containing components
        components = first_part.split()
        compositions = []
        for i in range(len(components)):
            if "%" in components[i]:  # Check if the component contains a percentage
                compositions.append(f"{components[i]} {components[i + 1]}")  # Pair % with material name

        return compositions
    else:
        # Step 3: Return an empty list if "Material" is not found
        return []
    


@handle_scraping_errors()
def get_all_image_urls(source: BeautifulSoup) -> list[str]:
    all_images = []
    images = source.find("div", id = "gallery-wrapper").find("div",class_="ProductGallery-gridWrapper MuiBox-root css-yghy1x").find_all("div",class_="MuiBox-root css-0")
    for image in images:
        new_images = image.find("img")["src"]
        all_images.append(new_images)
    return all_images




def get_image_url(source: BeautifulSoup) -> str:
    image = source.find("div", id = "gallery-wrapper").find("div",class_="ProductGallery-gridWrapper MuiBox-root css-yghy1x").find("div",class_="MuiBox-root css-0").find("img")["src"]
    return image




def is_product_available(source: BeautifulSoup) -> bool:
    return True




def parse_product_data(product_url: str, category_metadata: dict, source: BeautifulSoup) -> Product:
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
        # discount_percentage=get_discount_percentage(source),
        # price_after_discount=get_price_after_discount(source),
        color_name=get_color_name(source),
        colors=get_colors(source),
        # sizes=get_sizes(source),
        # rating=get_rating(source),
        # review_count=get_review_count(source),
        description=get_description(source),
        details=get_details(source),
        compositions=get_compositions(source),
        # sustainability_types=get_sustainability_types(source),
        # special_tag=get_special_tag(source),
        # published_date=get_published_date(source),
        # manufacturing_country=get_manufacturing_country(source),
        # private_labels=get_private_labels(source),
        # packs=get_packs(source),
        # season=get_season(source),
        # collab=get_collab(source),
        all_image_urls=get_all_image_urls(source),
        image_url=get_image_url(source)
    )

    return product





async def scrape_product(product_url: str, category_metadata: dict) -> Product:
    ### Code Here
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
