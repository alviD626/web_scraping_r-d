import re
import bs4
import json
import time
import math
import asyncio
import requests
import string
import traceback
import pandas as pd
import nest_asyncio
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


# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'}
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'



from main import get_source_by_playwright



# url = "https://www.mrporter.com/en-gb/mens/product/acne-studios/clothing/printed-t-shirts/exford-distressed-logo-print-cotton-jersey-t-shirt/1647597346626802"
# url = "https://www.mrporter.com/en-gb/mens/product/mr-p/clothing/casual-shorts/slim-fit-straight-leg-striped-cotton-bermuda-shorts/1647597334937901"
url = "https://www.mrporter.com/en-gb/mens/product/bottega-veneta/clothing/crew-necks/intrecciato-leather-trimmed-cashmere-blend-sweater/1647597343122618"



source = asyncio.get_event_loop().run_until_complete(get_source_by_playwright(url))




def get_pid(product_url: str) -> str:
    """Extract product ID from URL"""
    return product_url.split('/')[-1]

print("\n")
print(f"Pid: {get_pid(url)}")



def get_name(source: BeautifulSoup) -> str:
    """Extract product name"""
    name_element = source.find('p', {'class': 'ProductInformation88__name'})
    return name_element.get_text(strip=True)

print("\n")
print(f"Name: {get_name(source)}")




def get_currency(source: BeautifulSoup) -> str:
    """Extract currency symbol"""
    price_element = source.find('span', {'class': 'PriceWithSchema10__value'})
    currency = price_element.get_text(strip=True)[0]
    return currency

print("\n")
print(f"Currency: {get_currency(source)}")




def get_price(source: BeautifulSoup) -> float:
    """Extract price"""
    price_element = source.find('span', {'class': 'PriceWithSchema10__value'})
    price_text = price_element.get_text(strip=True).replace('£', '').strip().replace(",","")
    return float(price_text)

print("\n")
print(f"Price: {get_price(source)}")




def get_color_name(source: BeautifulSoup) -> str:
    """Extract color name"""
    color_element = source.find('span', {'class': 'ProductDetailsColours88__colourName'})
    return color_element.get_text(strip=True)

print("\n")
print(f"Main_color: {get_color_name(source)}")




def get_colors(source: BeautifulSoup) -> list[str]:
    """Extract available colors"""
    try:
        colors = []
        color_elements = source.find('div',{'class':'ProductDetailsColours88__coloursList'})
        if color_elements:
            new_color_elements = color_elements.find('ul',{'class':'ProductDetailsColours88__swatchList'}).find_all('li')
            for color in new_color_elements:
                color_name = color.find('a').get('title')
                if color_name:
                    colors.append(color_name)
            return list(set(colors))
        else:
            color_element = source.find('span', {'class': 'ProductDetailsColours88__colourName'}).get_text(strip=True)
            return [color_element]
    except Exception as e:
        print(e)

print("\n")
print(f"All_colors: {get_colors(source)}")




def get_sizes(source: BeautifulSoup) -> list[str]:
    """Extract available sizes"""
    sizes = []
    size_elements = source.find('ul', {'class': 'GridSelect11'}).find_all('label')
    for size in size_elements:
        sizes.append(size.get_text(strip=True))
    return sizes

print("\n")
print(f"Sizes: {get_sizes(source)}")




def get_description(source: BeautifulSoup) -> str:
    """Extract product description"""
    description = source.find('div', {'class': 'EditorialAccordion88__accordionContent--editors_notes'})
    if description:
        return description.get_text(strip=True)

print("\n")
print(f"Description: {get_description(source)}")




def get_details(source: BeautifulSoup) -> list[str]:
    """Extract product details"""
    details = []
    details_section = source.find('div', {'class': 'EditorialAccordion88__accordionContent--details_and_care'})
    if details_section:
        detail_items = details_section.find_all('li')
        details = [item.get_text(strip=True) for item in detail_items]
    return details

print("\n")
print(f"Details: {get_details(source)}")




def get_compositions(source: BeautifulSoup) -> list[str]:
    """Extract material compositions"""
    compositions = []
    details_section = source.find('div', {'class': 'EditorialAccordion88__accordionContent--details_and_care'})
    if details_section:
        for detail in details_section.find_all('li'):
            text = detail.get_text(strip=True)
            if '%' in text:
                new_composition = text.split(";")[0]
                compositions.extend([comp.strip() for comp in new_composition.split(',')])
    return compositions

print("\n")
print(f"Composition: {get_compositions(source)}")




def get_all_image_urls(source: BeautifulSoup) -> list[str]:
    """Extract all product image URLs"""
    image_urls = []
    # image_elements = source.find('div',{'class':'ImageCarousel88__mainCarousel ImageCarousel88__mainCarousel--allow2ndLevelZoom'}).find('div',{'class':'ImageCarousel88__viewport'}).find('ul',{'class':'ImageCarousel88__track'}).find_all('li')
    image_elements = source.find("div",class_="ProductDetailsPage88__wrapper").find("div",class_="ImageCarousel88 ProductDetailsPage88__imageCarouselGrid ProductDetailsPage88__imageCarouselGrid--sticky").find("div",class_="ImageCarousel88__thumbnails ProductDetailsPage88__imageCarouselThumbnails").find_all("div",class_="ImageCarousel88__thumbnail")
    for image in image_elements:
        image_url = image.find("picture").find("img")["src"]
        image_urls.append(f"https:{image_url}")
        # print(image_urls)
        return image_urls
print("\n")
print(f"All_images: {get_all_image_urls(source)}")




def get_image_url(source: BeautifulSoup) -> str:
    """Extract main product image URL"""
    first_image = source.find("div",class_="ImageCarousel88__thumbnail ImageCarousel88__thumbnail--active").find("picture").find('img')
    src = first_image.get('src')
    return f"https:{src}"
        

print("\n")
print(f"Main_image: {get_image_url(source)}")

