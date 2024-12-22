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



url = "https://us.carhartt-wip.com/collections/women-tshirts"
# url = "https://us.carhartt-wip.com/collections/women-tshirts?country=US"
# url = "https://us.carhartt-wip.com/products/w-noxon-pant-blue-stone-bleached-240"

# async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 50000) -> BeautifulSoup:
#     async with async_playwright() as playwright:
#         browser = await playwright.chromium.launch(headless=False)
#         context = await browser.new_context(user_agent=user_agent)
#         page = await context.new_page()
#         page.set_default_timeout(timeout)
#         try:
#             await page.goto(url, wait_until=wait_until)
#             time.sleep(5)

#             # Check if the country selection button is present and click it
#             if await page.locator("#md-form__select__country").count() > 0:
#                 await page.locator("#md-form__select__country").click()
#                 # time.sleep(5)

#                 # Select the US country option
#                 if await page.locator("#md-form__select__country__US").count() > 0:
#                     await page.locator("#md-form__select__country__US").click()
#                     await page.locator("#md-btn__form__onSubmit").click()
#                     # time.sleep(5)

#             await page.click('text=Accept')
#             # time.sleep(5)
#             await page.get_by_role("button",name="DISMISS").click()
#             # time.sleep(5)

#             # await page.locator("#md-form__select__country").click()
#             # time.sleep(5)
#             # await page.locator("#md-form__select__country__US").click()
#             # time.sleep(5)






#             # await page.locator("#md-btn__form__onSubmit").click()
#             # time.sleep(5)
#             # await page.goto(url, wait_until=wait_until)
#             source = BeautifulSoup(await page.content(), "html.parser")
#             # time.sleep(30)
#             # time.sleep(5)
#             print(source)
#             await browser.close()
#             return source
#         except Exception as e:
#             print(f"NetworkError getting page source for {url}: {e}")


async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 50000) -> BeautifulSoup:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)
            # time.sleep(5)

            # Check if the country selection button is present and click it
            if await page.locator("#md-form__select__country").count() > 0:
                await page.locator("#md-form__select__country").click()
                await page.locator("#md-form__select__country__US").click()
                await page.locator("#md-btn__form__onSubmit").click()
                # time.sleep(5)

            await page.click('text=Accept')
            await page.get_by_role("button",name="DISMISS").click()
            source = BeautifulSoup(await page.content(), "html.parser")
            await browser.close()
            return source
        except Exception as e:
            print(f"NetworkError getting page source for {url}: {e}")



# async def extract_product_urls(category_url: str) -> list[str]:
#     all_product_urls = []
#     source = await get_source_by_playwright(category_url)
#     total_products1 = source.find("div",id = "ss-fallback-filter-bar")
#     print(total_products1)
#     if total_products1 == None:
#         total_products = int(source.find("div",id = "no-ss-fallback-filter-bar").find("span").text.strip().split(" ")[0])
#         if total_products <=24:
#             product_urls = source.find_all("article")[1:]
#             for product_url in product_urls:
#                 new_urls = product_url.find("a")["href"]
#                 all_product_urls.append(new_urls)
#             return all_product_urls

#         else:
#             total_pages = math.ceil(total_products/24)
#             for i in range(1,total_pages+1):
#                 new_url = f"{category_url}&page={i}"
#                 source = await get_source_by_playwright(new_url)
#                 product_urls = source.find_all("article")[1:]
#                 for product_url in product_urls:
#                     new_urls = product_url.find("a")["href"]
#                     all_product_urls.append(f"https://us.carhartt-wip.com{new_urls}")
#             return all_product_urls
#     else:
#         total_products = int(total_products1.find("span").text.strip().split(" ")[0])
#         if total_products <=24:
#             product_urls = source.find_all("article")[1:]
#             for product_url in product_urls:
#                 new_urls = product_url.find("a")["href"]
#                 all_product_urls.append(new_urls)
#             return all_product_urls

#         else:
#             total_pages = math.ceil(total_products/24)
#             for i in range(1,total_pages+1):
#                 new_url = f"{category_url}&page={i}"
#                 source = await get_source_by_playwright(new_url)
#                 product_urls = source.find_all("article")[1:]
#                 for product_url in product_urls:
#                     new_urls = product_url.find("a")["href"]
#                     all_product_urls.append(f"https://us.carhartt-wip.com{new_urls}")
#             return all_product_urls


async def extract_product_urls(url: str) -> list[str]:
    all_product_urls = []
    source = await get_source_by_playwright(url)
    total_products1 = source.find("div",id = "ss-fallback-filter-bar")
    if total_products1 == None:
        total_products = int(source.find("div",id = "no-ss-fallback-filter-bar").find("span").text.strip().split(" ")[0])
        if total_products <=24:
            product_urls = source.find_all("article")[1:]
            for product_url in product_urls:
                new_urls = product_url.find("a")["href"]
                all_product_urls.append(new_urls)
            return all_product_urls

        else:
            total_pages = math.ceil(total_products/24)
            for i in range(1,total_pages+1):
                new_url = f"{url}?page={i}"
                source = await get_source_by_playwright(new_url)
                product_urls = source.find_all("article")[1:]
                for product_url in product_urls:
                    new_urls = product_url.find("a")["href"]
                    all_product_urls.append(f"https://us.carhartt-wip.com{new_urls}")
            return all_product_urls
    else:
        total_products = int(total_products1.find("span").text.strip().split(" ")[0])
        if total_products <=24:
            product_urls = source.find_all("article")[1:]
            for product_url in product_urls:
                new_urls = product_url.find("a")["href"]
                all_product_urls.append(new_urls)
            return all_product_urls

        else:
            total_pages = math.ceil(total_products/24)
            for i in range(1,total_pages+1):
                new_url = f"{url}?page={i}"
                source = await get_source_by_playwright(new_url)
                product_urls = source.find_all("article")[1:]
                for product_url in product_urls:
                    new_urls = product_url.find("a")["href"]
                    all_product_urls.append(f"https://us.carhartt-wip.com{new_urls}")
            return all_product_urls


print(asyncio.run(extract_product_urls(url)))