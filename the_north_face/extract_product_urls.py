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


from main import get_source_by_playwright

#links

# mens

# best seller
# url = "https://www.thenorthface.com/en-us/mens/mens-featured/mens-best-sellers-c226103"
# # new_arrival
# url = "https://www.thenorthface.com/en-us/mens/mens-featured/mens-new-arrivals-c226102"
# # jackets_vests
# url = "https://www.thenorthface.com/en-us/mens/mens-jackets-and-vests-c211702"
# # rain
# url = "https://www.thenorthface.com/en-us/mens/mens-jackets-and-vests-c211702"
# # insulated
# url = "https://www.thenorthface.com/en-us/mens/mens-jackets-and-vests/mens-insulated-and-down-c300771"
# # puffer
# url = "https://www.thenorthface.com/en-us/mens/mens-jackets-and-vests/mens-puffer-jackets-c829824"
# # windbreakers
# url = "https://www.thenorthface.com/en-us/mens/mens-jackets-and-vests/mens-windbreakers-c299290"
# # vests
# url = "https://www.thenorthface.com/en-us/mens/mens-jackets-and-vests/mens-vests-c299291"
# # softshell
# url = "https://www.thenorthface.com/en-us/mens/mens-jackets-and-vests/mens-softshells-c299287"
# # fleece
# url = "https://www.thenorthface.com/en-us/mens/mens-fleece-c299285"
# fullzip
# url = "https://www.thenorthface.com/en-us/mens/mens-fleece/mens-fleece-full-zip-c829791"
# # pullover
# url = "https://www.thenorthface.com/en-us/mens/mens-fleece/mens-fleece-full-zip-c829791"
# # top
# url = "https://www.thenorthface.com/en-us/mens/mens-tops-c211703"
# # t-shirts
# url = "https://www.thenorthface.com/en-us/mens/mens-tops-c211703"
# # hoodies & sweatshirts
# url = "https://www.thenorthface.com/en-us/mens/mens-tops/mens-hoodies-and-sweatshirts-c224211"
# # shirts & polos
# url = "https://www.thenorthface.com/en-us/mens/mens-tops/mens-shirts-and-polos-c224208"
# # active
# url = "https://www.thenorthface.com/en-us/mens/mens-tops/mens-active-tops-c224210"
# # bottoms
url = "https://www.thenorthface.com/en-us/mens/mens-bottoms-c211704"


# womens
url = "https://www.thenorthface.com/en-us/womens/womens-tops-c211720"
# tshit
# url = "https://www.thenorthface.com/en-us/womens/womens-tops/womens-t-shirts-c213341"
# # casual tops
# url = "https://www.thenorthface.com/en-us/womens/womens-tops/womens-casual-tops-c224261"
# shorts
# url = "https://www.thenorthface.com/en-us/womens/womens-bottoms/womens-shorts-c224274"

async def extract_product_urls(url):
    source = await get_source_by_playwright(url)
    id = url.split("-")[-1].split("c")[-1]
    # print(id)
    total_products = int(source.find("div",class_="container filter-panel__row filter-panel__row--redesign").find("div",class_="filter-panel__quantity filter-panel__quantity--redesign").text.strip().split(" ")[0])
    # print(total_products)
    all_urls = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Accept': 'application/json',
    }
    if total_products<=24:
        new_url = f"https://www.thenorthface.com/api/products/v1/catalog?start=0&count=24&sort=bestMatches&locale=en-us&filters=cgid={id}"
        response = requests.get(new_url, headers=headers)
        response_json = response.json()
        product_urls = response_json.get("products",[])
        for i in product_urls:
            new_url = i.get("fullPageUrl")
            all_urls.append(new_url)
        print(len(all_urls))
        # print(all_urls)
        return all_urls
    else:
        for scroll_number in range(0,total_products,24):
            new_url = f"https://www.thenorthface.com/api/products/v1/catalog?start={scroll_number}&count=24&sort=bestMatches&locale=en-us&filters=cgid={id}"
            response = requests.get(new_url, headers=headers)
            response_json = response.json()
            product_urls = response_json.get("products",[])
            for i in product_urls:
                new_url = i.get("fullPageUrl")
                all_urls.append(new_url)
        print(len(all_urls))
        # print(all_urls)
        return set(all_urls)

print(asyncio.run(extract_product_urls(url)))