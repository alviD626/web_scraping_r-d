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
from tqdm.notebook import tqdm  #for progress bar
from collections import OrderedDict
from playwright.async_api import async_playwright, expect, TimeoutError as PlaywrightTimeoutError, Error

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'



url = "https://us.dailypaperclothing.com/collections/women-all-tops"




async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 50000) -> BeautifulSoup:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)
            # await page.click("text = Stay on the US store")
            source = BeautifulSoup(await page.content(), "html.parser")
            time.sleep(10)
            total_products = int(source.find("span",class_="collection-count").find("span",class_="count-collectionitem").text.strip())
            number_of_scrolls = math.ceil(total_products/16)
            print(total_products)
            print(number_of_scrolls)
            for pages in range(1,number_of_scrolls+1):
                await page.keyboard.press("End")
                time.sleep(2)
            source = BeautifulSoup(await page.content(), "html.parser")
            all_urls = []
            product_urls = source.find("div",class_ = "collection-result").find("div",id = "collection-grid").find("div",id = "product-grid").find_all("div",class_="product-item")
            for urls in product_urls:
                new_urls = urls.find("a")["href"]
                all_urls.append(new_urls)

            print(len(all_urls))
            print(all_urls)
            # print(product_urls)
            await browser.close()
            return product_urls
        except Exception as e:
            print(f"NetworkError getting page source for {url}: {e}")
            return None
        

asyncio.run(get_source_by_playwright(url))