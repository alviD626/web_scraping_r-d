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

# url = "https://www.nobodyschild.com/collections/dresses"
url = "https://www.nobodyschild.com/collections/tops"


# async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 60000) -> BeautifulSoup:
#     async with async_playwright() as playwright:
#         browser = await playwright.chromium.launch(headless=False)
#         context = await browser.new_context(user_agent=user_agent)
#         page = await context.new_page()
#         page.set_default_timeout(timeout)
#         try:
#             await page.goto(url, wait_until=wait_until)
#             await page.get_by_role("button", name="CHANGE YOUR SHIPPING COUNTRY").click()
#             # time.sleep(5)
#             await page.wait_for_selector('#localization-select')
            
#             # Use selectOption to select the "United Kingdom (GBP £)" option by its value
#             await page.select_option('#localization-select', 'GB')
#             await page.locator("#onetrust-accept-btn-handler").click()
#             time.sleep(5)
#             # for x in range(1,20):
#             #     await page.keyboard.press("End")
#             #     time.sleep(2)
#             source = BeautifulSoup(await page.content(), "html.parser")
#             # links = source.find("div",class_="grid grid-cols-1 gap-y-0 gap-x-0 xs:grid-cols-2 sm:gap-x-8 sm:gap-y-8 sm:grid-cols-3 lg:grid-cols-4 cards-grid").find_all("div",class_="data-tagg-processed")
#             # all_links = []
#             # for link in links:
#             #     new_links = link.find("a")["href"]
#             #     all_links.append(new_links)
#             # print(len(all_links))
#             # print(all_links)
#             print(source)
        #     await browser.close()
        #     return source
        # except Exception as e:
        #     print(f"NetworkError getting page source for {url}: {e}")





async def extract_product_urls(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 90000) -> list[str]:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)
            await page.locator(".mx-16.cursor-pointer").click()
            # time.sleep(5)
            await page.get_by_role("button", name="CHANGE YOUR SHIPPING COUNTRY").click()
            # time.sleep(5)
            await page.wait_for_selector('#localization-select')

            # Use selectOption to select the "United Kingdom (GBP £)" option by its value
            await page.select_option('#localization-select', 'GB')
            await page.locator("#onetrust-accept-btn-handler").click()
            time.sleep(5)

            # Start the dynamic scroll loop
            all_links = []
            last_height = await page.evaluate("document.body.scrollHeight")
            
            while True:
                # Scroll to the bottom
                await page.mouse.wheel(0,1500)
                time.sleep(2)
                
                # Parse the current page content
                source = BeautifulSoup(await page.content(), "html.parser")
                links = source.find_all("a", class_="aspect-[3/4] h-full w-full bg-light-grey border-0")
                
                # Extract and append new product links
                for link in links:
                    new_links = link.get("href")
                    if new_links is None:
                        continue
                    final_links = new_links.split("collections")[-1]
                    all_links.append(f"https://www.nobodyschild.com{final_links}")

                # Check if more scrolling is possible
                new_height = await page.evaluate("document.body.scrollHeight")
                if new_height == last_height:
                    break  # Stop scrolling if we reached the bottom
                last_height = new_height

            print(f"Total links found: {len(all_links)}")

            await browser.close()
            return all_links
        except Exception as e:
            print(f"NetworkError getting page source for {url}: {e}")


print(asyncio.run(extract_product_urls(url)))