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
from tqdm.notebook import tqdm  #for progress bar
from collections import OrderedDict
from playwright.async_api import async_playwright, expect, TimeoutError as PlaywrightTimeoutError, Error

# import google translation
import googletrans
from googletrans import Translator
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'


url = "https://www.bilka.dk/brands/vrs/dametoej/pl/vrs-woman/"



async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 50000) -> BeautifulSoup:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)
            time.sleep(2)
            await page.get_by_role("button",name = "Accepter alle").click()
            time.sleep(5)
            source = BeautifulSoup(await page.content(), "html.parser")
            await browser.close()
            return source
        except Exception as e:
            print(f"NetworkError getting page source for {url}: {e}")
            return None
        


async def extract_product_url(url):
    source = await get_source_by_playwright(url)
    product_urls = []
    total_products = int(source.find("div",class_="paging mt-8").find("div",class_="paging-controls").find("div",class_="progress-wrapper").get_text(strip=True).split(" ")[-1])
    links = source.find("div",class_="products").find("div",class_="row products__row").find_all("div",class_="products__item col col-fixed-1 col-sm-fixed-2 col-md-fixed-3 col-lg-fixed-3 col-xl-fixed-3")
    if total_products < 60:
        for link in links:
            new_link = link.find("a").get("href")
            product_urls.append(f"https://www.bilka.dk{new_link}")
        print(len(product_urls))
        print(len(set(product_urls)))
        return product_urls
    else:
        pages = math.ceil(total_products/60)
        for i in range(0,pages):
            new_url = f"{url}?p={i}"
            source = await get_source_by_playwright(new_url)
            for link in links:
                new_link = link.find("a").get("href")
                product_urls.append(f"https://www.bilka.dk{new_link}")
        print(len(product_urls))
        print(len(set(product_urls)))
        return product_urls

        

print(asyncio.run(extract_product_url(url)))