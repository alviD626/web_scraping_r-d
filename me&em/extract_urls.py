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

url = "https://www.meandem.com/lounge-in-style"

async def extract_urls(url):
    all_urls = []
    source = await get_source_by_playwright(url)
    total_products = int(source.find("div",class_="mx-auto flex w-full max-w-[414px] flex-col gap-8 pb-16").find("span",class_="type-body-sm text-center").find_all("strong")[-1].get_text(strip=True))
    if total_products < 72:
        product_urls = source.find("section", class_="site-container spacing-y-md grid gap-12").find("ul",class_="grid-base grid-cols-12 gap-y-16").find_all("li")
        for product_url in product_urls:
            new_urls = product_url.find("a")["href"]
            all_urls.append(f"https://www.meandem.com{new_urls}")
        return all_urls
    else:
        total_pages = math.ceil(total_products/72)
        for pages in range(1,total_pages+1):
            new_pages = f"{url}?page={pages}"
            source = await get_source_by_playwright(new_pages)
            product_urls = source.find("section", class_="site-container spacing-y-md grid gap-12").find("ul",class_="grid-base grid-cols-12 gap-y-16").find_all("li")
            for product_url in product_urls:
                new_urls = product_url.find("a")["href"]
                all_urls.append(f"https://www.meandem.com{new_urls}")
        return all_urls

print(asyncio.run(extract_urls(url)))
