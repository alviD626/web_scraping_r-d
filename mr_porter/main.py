import random
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


# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'}
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.62 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/116.0.5845.115 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.126 Mobile Safari/537.36"
]




# url = "https://www.mrporter.com/en-gb/mens/clothing/t-shirts"
# url = "https://www.mrporter.com/en-gb/mens/product/acne-studios/clothing/printed-t-shirts/exford-distressed-logo-print-cotton-jersey-t-shirt/1647597346626802"




async def get_source_by_playwright(url: str, user_agent: str = None, wait_until: str = 'domcontentloaded', timeout: int = 50000) -> BeautifulSoup:
    user_agent = user_agent or random.choice(USER_AGENTS)
    async with async_playwright() as playwright:
        # browsers = ["chromium", "firefox"]
        # for browser_type in browsers:
            try:
                browser = await playwright.firefox.launch(headless=False)
                # browser = await getattr(playwright, browser_type).launch(headless=False)
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
            except Exception as e:
                print(f"Error launching browser: {e}")
                return None
                # If both fail, return None
        # print(f"All browsers failed to load {url}.")
        # return None
        



# print(asyncio.run(get_source_by_playwright(url)))