import re
import bs4
import json
import time
import math
import asyncio
import nest_asyncio
import requests
import string
import traceback
import pandas as pd
nest_asyncio.apply()
import concurrent.futures
from datetime import datetime
from json import JSONDecodeError
from unicodedata import normalize
from bs4 import BeautifulSoup
#from stop_words import get_stop_words
from requests.exceptions import ConnectionError
from playwright.sync_api import sync_playwright
from collections import OrderedDict
from playwright.async_api import async_playwright, expect, TimeoutError as PlaywrightTimeoutError, Error



from main import get_source_by_playwright


url = "https://www.prada.com/ww/en/p/jersey-t-shirt-with-embroidered-triangle/35838R_16DV_F0002_S_162"


source = asyncio.get_event_loop().run_until_complete(get_source_by_playwright(url))


# def get_pid(url: str) -> str:
#     """Extract product ID from URL"""
#     return url.split('/')[-1]


# def get_name(source: BeautifulSoup) -> str:
#     """Extract product name"""
#     name_elem = source.find('h1', {'class': 'text-title-big'})
#     return name_elem.text.strip()


# def get_currency(source: BeautifulSoup) -> str:
#     """Extract currency symbol"""
#     # Default currency for Prada WW site is USD
#     return "$"


# def get_price(source: BeautifulSoup) -> float:
#     """Extract price value"""
#     # Implementation would require javascript rendered price
#     # This would need additional handling with Selenium/Playwright
#     return None


# def get_color_name(source: BeautifulSoup) -> str:
#     """Extract color name"""
#     color_elem = source.find('div', string='Color')
#     if color_elem:
#         return color_elem.find_next_sibling().text.strip()
#     return None

# def get_colors(source: BeautifulSoup) -> list[str]:
#     """Extract available colors"""
#     colors = []
#     color_links = source.find_all('a', {'data-test': 'colorOption'})
#     for color in color_links:
#         colors.append(color.get('title'))
#     return colors


# def get_description(source: BeautifulSoup) -> str:
#     """Extract product description"""
#     desc_elem = source.find('div', {'element': 'product-details'})
#     if desc_elem:
#         return desc_elem.find('div', {'class': 'flex-col'}).text.strip()
#     return ''

# def get_details(source: BeautifulSoup) -> list[str]:
#     """Extract product details"""
#     details = []
#     details_container = source.find('div', {'class': 'flex-col gap-4'})
#     if details_container:
#         for detail in details_container.find_all('li'):
#             details.append(detail.text.strip())
#     return details

# def get_compositions(source: BeautifulSoup) -> list[str]:
#     """Extract material compositions"""
#     compositions = []
#     materials_section = source.find('div', {'element': 'materials-and-care'})
#     if materials_section:
#         materials = materials_section.text.strip()
#         # Would need additional parsing logic based on actual material format
#         compositions.append(materials)
#     return compositions


# def get_all_image_urls(source: BeautifulSoup) -> list[str]:
#     """Extract all product image URLs"""
#     images = []
#     img_elements = source.find_all('img', {'class': 'pdp-product-img'})
#     for img in img_elements:
#         if img.get('srcset'):
#             # Get first image URL from srcset
#             src = img['srcset'].split(',')[0].split(' ')[0]
#             images.append(src)
#     return images



# def get_image_url(source: BeautifulSoup) -> str:
#     """Extract main product image URL"""
#     img_elem = source.find('img', {'class': 'pdp-product-img'})
#     if img_elem and img_elem.get('srcset'):
#         return img_elem['srcset'].split(',')[0].split(' ')[0]
#     return ''


def description(source):
    script_file = source.find("script", id = "jsonldProduct").get_text(strip=True)
    response_data = json.loads(script_file)
    description = response_data.get("description")
    return description

def details(source):
    all_details = []
    init_details = source.find("div", class_ = "product-details-wrapper").find("ul").find_all("li")
    for d in init_details:
        new_details = d.get_text(strip = True)
        all_details.append(new_details)
    return all_details


def currency(source):
    script_file = source.find("script", id = "jsonldProduct").get_text(strip=True)
    response_data = json.loads(script_file)
    currency = response_data.get("offers").get("priceCurrency")
    return currency


def price(source):
    script_file = source.find("script", id = "jsonldProduct").get_text(strip=True)
    response_data = json.loads(script_file)
    price = response_data.get("offers").get("price")
    return price

def sizes(source):
    all_sizes = []
    init_sizes = source.find("div", class_ = "size-picker-drawer").find("ul").find_all("li")
    for d in init_sizes:
        new_sizes = d.get_text(strip = True)
        all_sizes.append(new_sizes)
    return all_sizes


def color(source):
    main_color = source.find("div",class_="w-full flex flex-col items-start").find_all("p")[-1].get_text(strip=True)
    return main_color

def colors(source):
    colors = source.find("div",class_="w-full flex flex-col items-start").find_all("p")[-1].get_text(strip=True)
    return [colors]





# print(images(source))