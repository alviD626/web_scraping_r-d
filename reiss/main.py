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


url = "https://www.reiss.com/us/en/shop/gender-women-productaffiliation-topssweats-0"


# async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 30000) -> BeautifulSoup:
#     async with async_playwright() as playwright:
#         browser = await playwright.chromium.launch(headless=False)
#         context = await browser.new_context(user_agent=user_agent)
#         page = await context.new_page()
#         page.set_default_timeout(timeout)
#         try:
#             await page.goto(url, wait_until=wait_until)
#             source = BeautifulSoup(await page.content(), "html.parser")
#             all_urls = []
#             total_products = int(source.find("div",id = "plp-seo-heading").find("span").text.strip().replace("(","").replace(")",""))
#             print(total_products)
#             if total_products<=12:
#                 product_urls = source.find("div",class_="MuiGrid-root MuiGrid-container plp-product-grid-wrapper plp-1crp0ll").find("div",class_="MuiGrid-root MuiGrid-container plp-1t08jfd").find_all("div",class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-4 MuiGrid-grid-lg-3 MuiGrid-grid-xl-3 plp-ngi0wf")
#                 for product in product_urls:
#                     new_url = product.find("a")["href"]
#                     all_urls.append(new_url)
#                 print(all_urls)
#                 print(len(all_urls))
#                 return all_urls
#             else:
#                 scroll_number = math.ceil(total_products/12)
#                 print(scroll_number)
#                 for _ in range(1, scroll_number+1):
#                     await page.mouse.wheel(0,1550)
#                     # print('scrolling...',x)
                    
#                     await asyncio.sleep(2)
#                 source = BeautifulSoup(await page.content(),"html.parser")
                
#                 product_urls = source.find("div",class_="MuiGrid-root MuiGrid-container plp-product-grid-wrapper plp-1crp0ll").find("div",class_="MuiGrid-root MuiGrid-container plp-1t08jfd").find_all("div",class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-4 MuiGrid-grid-lg-3 MuiGrid-grid-xl-3 plp-ngi0wf")
#                 for product in product_urls:
#                     new_url = product.find("a")["href"]
#                     all_urls.append(new_url)
#                 print(all_urls)
#                 print(len(all_urls))
#             # print(product_urls)
#             time.sleep(10)
#             await browser.close()
#             # print(source)
#             return all_urls
#         except Exception as e:
#             print(f"NetworkError getting page source for {url}: {e}")
#             return None
        

# asyncio.run(get_source_by_playwright(url))



def extract_source(url):
    response = requests.get(url,headers = headers).text
    source = BeautifulSoup(response,"html.parser")
    return source

print(extract_source(url))