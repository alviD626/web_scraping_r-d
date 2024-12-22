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

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'


from main import get_source_by_playwright

url = "https://www.meandem.com/merino-stretch-rib-two-way-zip-jumper-cream"


BASE_URL= "https://www.meandem.com/"


source = asyncio.get_event_loop().run_until_complete(get_source_by_playwright(url))

def get_pid(url: str) -> str:
    """Extract product ID from URL"""
    # Example URL: /brushed-cashmere-v-neck-vest-sapphire-blue
    return url.split('/')[-1]

print(f"ID: {get_pid(url)}")
print("\n\n")

def get_name(source: BeautifulSoup) -> str:
    """Extract product name"""
    name_elem = source.find("h3", {"class": "product-title"})
    return name_elem.text.strip()
    
print(f"Name: {get_name(source)}")
print("\n\n")

def get_currency(source: BeautifulSoup) -> str:
    """Extract currency symbol"""
    price_elem = source.find("div", {"class": "HeaderAndPrice-block"})
    return price_elem.text.strip()[0] if price_elem else "£"
    
print(f"Currency: {get_currency(source)}")
print("\n\n")

def get_price(source: BeautifulSoup) -> float:
    """Extract price"""
    price_elem = source.find("div", {"class": "HeaderAndPrice-block"})
    if price_elem:
        price_text = price_elem.text.strip()[1:]  # Remove currency symbol
        return float(price_text)
    
print(f"Price: {get_price(source)}")
print("\n\n")


def get_color_name(source: BeautifulSoup) -> str:
    """Extract main color name"""
    color_elem = source.find("div", id="color-selector-block-color")
    if color_elem:
        return color_elem.find("span", {"class": "css-4k385d"}).text.strip()

print(f"Color: {get_color_name(source)}")
print("\n\n")


def get_colors(source: BeautifulSoup) -> list[str]:
    """Extract all available colors"""
    colors = []
    color_links = source.find_all("a", {"data-evergage-color": True})
    for link in color_links:
        color = link["data-evergage-color"]
        colors.append(color)
    return colors

print(f"All Colors: {get_colors(source)}")
print("\n\n")


def get_description(source: BeautifulSoup) -> str:
    """Extract product description"""
    desc_elem = source.find("h5", {"class": "HeaderAndPrice-productDescription"})
    return desc_elem.text.strip() if desc_elem else ""

print(f"Description: {get_description(source)}")
print("\n\n")


def get_details(source: BeautifulSoup) -> list[str]:
    """Extract product details"""
    details = []
    details_elem = source.find("div", id="product-details-accordion")
    if details_elem:
        details_text = details_elem.find("p", {"class": "css-g9ki7z"}).text
        details = [d.strip() for d in details_text.split("\n") if d.strip()]
    return details

print(f"Details: {get_details(source)}")
print("\n\n")



def get_compositions(source: BeautifulSoup) -> list[str]:
    """Extract material compositions"""
    details = get_details(source)
    compositions = []
    for detail in details:
        if "Material:" in detail:
            material_text = detail.split("Material:")[1].strip()
            # Split by percentage sign and pair with next word
            parts = material_text.split("%")
            for i in range(len(parts)-1):  
                percentage = parts[i].strip().split()[-1]
                material = parts[i+1].strip().split()[0]
                compositions.append(f"{percentage}% {material}")
    return compositions

print(f"Composition: {get_compositions(source)}")
print("\n\n")



def get_all_image_urls(source: BeautifulSoup) -> list[str]:
    """Extract all product image URLs"""
    images = []
    gallery = source.find("div", {"class": "ProductGallery-gridWrapper"})
    if gallery:
        for img in gallery.find_all("img"):
            if "src" in img.attrs:
                images.append(img["src"])
    return images

print(f"All Images: {get_all_image_urls(source)}")
print("\n\n")



def get_image_url(source: BeautifulSoup) -> str:
    """Extract main product image URL"""
    images = get_all_image_urls(source)
    return images[0] if images else ""

print(f"Main_image: {get_image_url(source)}")


# print(get_name(source))