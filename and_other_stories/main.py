# utility function
import re
import bs4
import json
import time
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


url = "https://www.stories.com/en_gbp/clothing/dresses.html"

async def get_source_by_playwright_p_links(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 10000) -> BS:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)
            await page.locator("#onetrust-accept-btn-handler").click()
            await page.locator("#countryNameHeader").click()
            # await page.get_by_label("United Kingdom").click()
            await page.locator('a:has-text("United Kingdom")').click()
            
            await page.goto(url, wait_until=wait_until)
            source = BS(await page.content(), "html.parser")
            # time.sleep(5)
            await browser.close()
            # print(source)
            return source
        except Exception as e:
            print(f"NetworkError getting page source for {url}: {e}")
            return None
        


async def extract_product_urls(url):
    all_links = []
    source = asyncio.run(get_source_by_playwright_p_links(url))
    pages = source.find("noscript")
    if pages is None:
        total_links = source.find("div",id="reloadProducts").find_all("div",class_="o-product producttile-wrapper")
        for link in total_links:
            all_links.append(link.find("a").get("href"))
        return all_links
    else:
        total_pages = int(source.find("noscript").find("ul").find_all("li")[-1].text.strip().split(" ")[-1])

        for page in range(1,total_pages+1):
            new_pages = f"{url}?page={page}"
            # all_pages.append(new_pages)
            source = asyncio.run(get_source_by_playwright_p_links(new_pages))
            total_links = source.find("div",id="reloadProducts").find_all("div",class_="o-product producttile-wrapper")

            for link in total_links:
                all_links.append(link.find("a").get("href"))
        return all_links

# extract_product_pages(url)



# asyncio.run(get_source_by_playwright_p_links(url))
print(asyncio.run(extract_product_urls(url)))