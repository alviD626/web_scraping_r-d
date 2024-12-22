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


url = "https://www.prada.com/ww/en/womens/ready-to-wear/dresses/c/10050EU"

async def extract_urls(url: str):
            all_urls = []
            source = await get_source_by_playwright(url)
            total_products = int(source.find("div",class_="category-and-sort-wrapper").find("div",class_="ais-Stats").find("p",class_="text-paragraph-small uppercase lg:font-medium").get_text(strip=True).split(" ")[0])

            if total_products < 24:
                links = source.find("div", class_ = "ais-InfiniteHits plp-results-container").find("ol", id="PLPComponent").find_all("li",class_="w-full h-auto lg:h-full")
                for link in links:
                    new_urls = link.find("a")["href"]
                    all_urls.append(f"https://www.prada.com{new_urls}")
                # print(len(all_urls))
                # print(len(set(all_urls)))
                return all_urls
            else:
                total_pages = math.ceil(total_products/24)
                for i in range(1,total_pages+1):
                    new_url = f"{url}/page/{i}"
                    source = await get_source_by_playwright(new_url)
                    links = source.find("div", class_ = "ais-InfiniteHits plp-results-container").find("ol", id="PLPComponent").find_all("li",class_="w-full h-auto lg:h-full")
                    for link in links:
                        new_urls = link.find("a")["href"]
                        all_urls.append(f"https://www.prada.com{new_urls}")
                # print(len(all_urls))
                # print(len(set(all_urls)))
                return all_urls
        

print(asyncio.run(extract_urls(url)))