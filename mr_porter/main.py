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




# url = "https://www.mrporter.com/en-gb/mens/clothing/t-shirts"
# url = "https://www.mrporter.com/en-gb/mens/product/acne-studios/clothing/printed-t-shirts/exford-distressed-logo-print-cotton-jersey-t-shirt/1647597346626802"




async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 50000) -> BeautifulSoup:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)
            time.sleep(5)
            source = BeautifulSoup(await page.content(), "html.parser")
            await browser.close()
            return source
        except Exception as e:
            print(f"NetworkError getting page source for {url}: {e}")
            return None
        



# print(asyncio.run(get_source_by_playwright(url)))