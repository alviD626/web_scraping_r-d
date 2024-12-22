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


# url = "https://www.oliverbonas.com/fashion/dresses"
url = "https://www.oliverbonas.com/fashion/all"



async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 50000) -> BeautifulSoup:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)
            time.sleep(2)
            await page.locator("#onetrust-accept-btn-handler").click()
            time.sleep(4)
            await page.locator("button.pos-absolute.right-0.z-1").click()
            time.sleep(2)
            source = BeautifulSoup(await page.content(), "html.parser")
            total_products = source.find("div",class_="wrap-x wrap-l").find("span",class_="p-l-2 col-13 lh-2 p2 va-b no-wrap w-12-s p-l-0-s").get_text(strip=True)
            print(total_products)
            # time.sleep(5)
            await browser.close()
            return source
        except Exception as e:
            print(f"NetworkError getting page source for {url}: {e}")


print(asyncio.run(get_source_by_playwright(url)))