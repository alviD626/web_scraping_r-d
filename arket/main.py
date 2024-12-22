# utility function
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

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'

url = "https://www.arket.com/sv_se/women/tops/t-shirts.html"


# async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 30000) -> BeautifulSoup:
#     async with async_playwright() as playwright:
#         browser = await playwright.chromium.launch(headless=False)
#         context = await browser.new_context(user_agent=user_agent)
#         page = await context.new_page()
#         page.set_default_timeout(timeout)
#         try:
#             await page.goto(url, wait_until=wait_until)
#             await page.locator("#onetrust-accept-btn-handler").click()
#             await page.locator("span.a-icon-lg-close-circle").first.click()
#             await page.locator("button.a-button-nostyle.info-icon.tooltip-trigger[aria-label='information']").click()
#             await page.locator("#navMenuShippingLink").click()
#             await page.locator('a:has-text("United Kingdom")').click()

#             await page.goto(url, wait_until=wait_until)
#             source = BeautifulSoup(await page.content(), "html.parser")
#             time.sleep(15)
#             await browser.close()
#             print(source)
#             return source
#         except Exception as e:
#             print(f"NetworkError getting page source for {url}: {e}")
#             return None


# async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 30000) -> BeautifulSoup:
#     async with async_playwright() as playwright:
#         browser = await playwright.chromium.launch(headless=True)
#         context = await browser.new_context(user_agent=user_agent)
#         page = await context.new_page()
#         page.set_default_timeout(timeout)
#         try:
#             await page.goto(url, wait_until=wait_until)
#             source = BeautifulSoup(await page.content(), "html.parser")
#             total_products = int(source.find("button",class_="a-button-nostyle mobile-filter-btn filter-link i18n").find("span",class_="total-items i18n").text.split(" ")[0])
#             roll = math.ceil(total_products/12)
#             for x in range(1,roll+1):
#                 await page.mouse.wheel(0,15000)
#                 await page.wait_for_load_state(wait_until)
#                 time.sleep(2)
#                 print(f"Scorlling to height: {x}")

#             # await page.goto(url, wait_until=wait_until)
#             source = BeautifulSoup(await page.content(), "html.parser")
#             links = source.find("div",id="reloadProducts").find_all("div",class_="o-product productTrack")
#             all_links = []
#             for link in links:
#                 new_links = link.find("a")["href"]
#                 all_links.append(new_links)
#             await browser.close()
#             print(all_links)
#             print(len(all_links))
#             return all_links
#         except Exception as e:
#             print(f"NetworkError getting page source for {url}: {e}")
#             return None
        

async def get_source_by_playwright(url: str, user_agent: str, wait_until: str = 'domcontentloaded', timeout: int = 30000) -> BeautifulSoup:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)

            # scroll to the bottom:
            _prev_height = -1
            _max_scrolls = 100
            _scroll_count = 0
            while _scroll_count < _max_scrolls:
                # Execute JavaScript to scroll to the bottom of the page
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                # Wait for new content to load (change this value as needed)
                await page.wait_for_timeout(1000)
                # Check whether the scroll height changed - means more pages are there
                new_height = await page.evaluate("document.body.scrollHeight")
                if new_height == _prev_height:
                    break
                _prev_height = new_height
                _scroll_count += 1

            source = BeautifulSoup(await page.content(), "html.parser")
            # links = source.find("div", id="reloadProducts").find_all("div", class_="o-product productTrack")
            # all_links = [link.find("a")["href"] for link in links]
            # print(all_links)
            # print(len(all_links))
            # print()

            # source = BeautifulSoup(await page.content(), "html.parser")
            # links = source.find("div", id="reloadProducts").find_all("div", class_="o-product productTrack")
            # all_links = [link.find("a")["href"] for link in links]

            await browser.close()
            # print(all_links)
            # print(len(all_links))
            # return all_links
            return source

        except Exception as e:
            print(f"NetworkError getting page source for {url}: {e}")
            return None



print(asyncio.run(get_source_by_playwright(url,user_agent)))