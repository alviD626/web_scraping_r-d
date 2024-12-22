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


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'}
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'

# ?pageNumber=2

from main import get_source_by_playwright



url = "https://www.mrporter.com/en-gb/mens/clothing/t-shirts"

async def extract_urls(url):
    source = await get_source_by_playwright(url)
    product_urls = []
    total_products = int(source.find("main",class_="content").find("section",class_="ProductListingPage0__gutterWrapper").find("div",class_="ProductListingPage0__filterResults").find("span",class_="ProductListingPage0__totalProducts").get_text(strip=True).split(" ")[0].replace(",",""))
    print(total_products)

    if total_products < 60:
        links = source.find_all("div",class_="ProductList0__productItemContainer")
        for link in links:
            new_link = link.find("a").get("href")
            product_urls.append(f"https://www.mrporter.com{new_link}")
        print(len(product_urls))
        print(len(set(product_urls)))
        return product_urls
    else:
        pages = math.ceil(total_products/60)
        for i in range(1,pages+1):
            new_url = f"{url}?pageNumber={i}"
            source = await get_source_by_playwright(new_url)
            links = source.find_all("div",class_="ProductList0__productItemContainer")
            for link in links:
                new_link = link.find("a").get("href")
                product_urls.append(f"https://www.mrporter.com{new_link}")
        print(len(product_urls))
        print(len(set(product_urls)))
        return product_urls
    

    
print(asyncio.run(extract_urls(url)))