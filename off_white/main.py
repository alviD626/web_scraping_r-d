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



url = "https://www.off---white.com/en-bd/sets/new-in"



async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 30000) -> BS:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)
            time.sleep(20)
            # await page.get_by_text("Materials").dblclick()
            # time.sleep(2)
            source = BS(await page.content(), "html.parser")
            await browser.close()
            return source
        except Exception as e:
            print(f"NetworkError getting page source for {url}: {e}")
            return None



async def page_numbers(url: str):
    source = await get_source_by_playwright(url)
    # result_key = url.split(".com")[-1]
    # print(result_key)
    code_to_remove = """window.__PRELOADED_STATE__ = """
    raw_script = source.find_all("script",type = "text/javascript")
    for script in raw_script:
        if """window.__PRELOADED_STATE__ = """ in script.text:
            script_content = script.string
            modified_script_content = script_content.replace(code_to_remove, "")
            find_json = json.loads(modified_script_content)
            result_key = find_json.get("listing").get("hash")
            total_pages = find_json.get("entities").get("searchResults").get(result_key).get("products").get("totalPages")
            return total_pages



async def get_product_links(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 60000) -> BS:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)
            time.sleep(20)
            source = BS(await page.content(), "html.parser")
            link_pages = await page_numbers(url)
            all_product_urls = []
            for number in range(1,link_pages+1):
                print(number)
                await page.goto(f"{url}?pageindex={number}", wait_until=wait_until)
                source = BS(await page.content(), "html.parser")
                new_urls = source.find("ul",class_="emnvohd8 css-ivk6ru e1b4emfh1").find_all("li")
                for product_url in new_urls:
                    update_product_url = product_url.find("a").get("href")
                    all_product_urls.append(f"https://www.off---white.com{update_product_url}")
            print(len(all_product_urls))
            await browser.close()
            return all_product_urls
        except Exception as e:
            print(f"Error getting page source for {url}: {e}")
            return None
        


asyncio.run(get_product_links(url))