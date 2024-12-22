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
from bs4 import BeautifulSoup as BS
#from stop_words import get_stop_words
from requests.exceptions import ConnectionError
from playwright.sync_api import sync_playwright
from tqdm.notebook import tqdm  #for progress bar
from collections import OrderedDict
from playwright.async_api import async_playwright, expect, TimeoutError as PlaywrightTimeoutError, Error

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'



url = "https://www.farfetch.com/bd/shopping/women/tops-1/items.aspx"

async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 30000) -> BS:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)
            source = BS(await page.content(), "html.parser")
            # time.sleep(5)
            await browser.close()
            return source
        except Exception as e:
            print(f"NetworkError getting page source for {url}: {e}")
            return None
        

# def product_link(url):
#     page_number = 1
#     all_links = []

#     while True:
#         current_url = f"{url}?page={page_number}"
#         source = asyncio.get_event_loop().run_until_complete(get_source_by_playwright(current_url))
#         get_json = source.find("script", type="application/ld+json").get_text()
#         link_json = json.loads(get_json)
#         get_link = link_json.get("itemListElement", [])
#         p_links = []

#         for init_link in get_link:
#             new_link = init_link.get("offers")
#             p_links.append(new_link)

#         links = [f"https://www.farfetch.com{final_link.get('url')}" for final_link in p_links]
#         all_links.extend(links)

#         if len(links) < 96:  # If the page has less than 96 product links, stop scraping
#             break

#         page_number += 1

#     return all_links

def product_link(url):
    source = asyncio.get_event_loop().run_until_complete(get_source_by_playwright(url))
    total_products = int(source.find("div",class_="ltr-1vyajtf").find("span",class_="ltr-gq26dl").text.split(" ")[-1])
    print(total_products)
    result = []
    init_links = source.find("div",class_="ltr-1qtmqf1").find("ul", id = "catalog-grid").find_all("li")
    for i in init_links:
        new_link = i.find("a")['href']
        result.append(f"https://www.farfetch.com{new_link}")
    print(result) 
    return result
# asyncio.run(get_source_by_playwright(url))
product_link(url)