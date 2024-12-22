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


# url = "https://www.arket.com/en_gbp/women/loungewear/product.cotton-stretch-t-shirt-white.1223919002.html"
# url = "https://www.arket.com/en_gbp/women/tops/t-shirts.html"
url = " https://www.arket.com/en_gbp/women/knitwear/crew-neck/product.alpaca-wool-blend-jumper-black.1248555003.html"



async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 30000) -> BeautifulSoup:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)
            time.sleep(5)
            await page.keyboard.press("End")
            await page.locator('button.a-button-nostyle.close-click-area').click()
            time.sleep(2)
            await page.locator("#noTransactionalClick").click()
            time.sleep(2)
            await page.locator('a[data-country="GB"]').click()
            time.sleep(2)
            source = BeautifulSoup(await page.content(), "html.parser")
            await browser.close()
            return source
        except Exception as e:
            print(f"NetworkError getting page source for {url}: {e}")
            return None

print(asyncio.run(get_source_by_playwright(url)))
# source = asyncio.get_event_loop().run_until_complete(get_source_by_playwright(url))

# ok
# def get_pid(source: BeautifulSoup) -> str:
#     return source.find("div",class_="id-el").find("span",class_="pdp-value for-highlight").text.strip()


#ok
# def get_name(source: BeautifulSoup) -> str:
    # return source.find("h1",class_="a-heading-3").text.strip()

#ok
# def get_currency(source: BeautifulSoup) -> str:
#     return source.find("span",id ="productPrice").text[0]

#ok
# def get_price(source: BeautifulSoup) -> str:
#     return source.find("span",id ="productPrice").text.replace("£","")


# def get_price(source: BeautifulSoup) -> str:
#     init_price =  source.find("div",id = "product-price").find("span",class_="is-deprecated")
#     if init_price is None:
#         update_price = source.find("span",id ="productPrice").text.replace("£","")
#         return update_price
#     else:
#         update_price = init_price.get_text().replace("£","")
#         return update_price


def get_price_after_discount(source: BeautifulSoup) -> str:
    init_price =  source.find("div",id = "product-price").find("span",class_="is-deprecated")
    if init_price is None:
        return ""
    else:
        update_price = source.find("span",id ="productPrice").text.replace("£","")
        return update_price


# print(get_price(source))

#ok
# def get_color_name(source: BeautifulSoup) -> str:
#     return source.find("div",class_="swatch-collapse-container").find("div",class_="a-swatch js-swatch is-selected")["data-item-value"]


#ok
# def get_colors(source: BeautifulSoup) -> list[str]:
#     colors = source.find("div",class_="swatch-collapse-container").find("div",class_="a-swatch js-swatch is-selected")["data-item-value"]
#     return [colors]


#ok
# def get_sizes(source: BeautifulSoup) -> list[str]:
#     sizes = source.find("div",id="size").find_all("button")
#     all_sizes = []
#     for size in sizes:
#         new_size = size.find("span").text.strip()
#         all_sizes.append(new_size)
#     return all_sizes


#ok
# def get_description(source: BeautifulSoup) -> str:
#     response_txt = source.find("script",id="product-schema").text
#     response_json = json.loads(response_txt)
#     description = response_json.get("description")
#     description_text = BeautifulSoup(description, "html.parser")
#     description = description_text.get_text().strip()
#     return description


# ok
# def get_compositions(source: BeautifulSoup) -> list[str]:
#     init_comp = source.find("div",class_="list-container").find("ul",id="details-list")
#     comp_list = init_comp.find_all("li")
#     comp_dict = []
#     for li in comp_list:
#         if "%" in li.get_text(strip=True):
#             new_composition = li.get_text(strip=True).split(",")
#             for i in range(len(new_composition)):
#                 new_composition[i] = new_composition[i].strip()
#             return new_composition



# ok
# def get_all_image_urls(source: BeautifulSoup) -> list[str]:
#     response_txt = source.find("script",id="product-schema").text
#     response_json = json.loads(response_txt)
#     images = response_json.get("image")
#     return images


#ok
# def get_image_url(source: BeautifulSoup) -> str:
#     response_txt = source.find("script",id="product-schema").text
#     response_json = json.loads(response_txt)
#     image = response_json.get("image")[0]
#     return image


