# utility function
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
from bs4 import BeautifulSoup as BS
#from stop_words import get_stop_words
from requests.exceptions import ConnectionError
from playwright.sync_api import sync_playwright
from tqdm.notebook import tqdm  #for progress bar
from collections import OrderedDict
from playwright.async_api import async_playwright, expect, TimeoutError as PlaywrightTimeoutError, Error

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'



url = "https://www.stoneisland.com/it/stone-island/polo-t-shirts"

async def get_source_by_playwright(url: str, user_agent: str = user_agent, wait_until: str = 'domcontentloaded', timeout: int = 30000) -> BS:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        page.set_default_timeout(timeout)
        try:
            await page.goto(url, wait_until=wait_until)
            # await page.content()
            # await page.get_by_role("button",name="NO").dblclick()
            await page.get_by_role("button",name="Accetta solo i cookie tecnici").dblclick()
            for _ in range(1, 4):
                await page.mouse.wheel(0,1500)
                # print('scrolling...',x)
                
                await asyncio.sleep(2)
                await page.get_by_role("button",name="Mostra altri").dblclick()
            
            source = BS(await page.content(), "html.parser")
            await browser.close()
            return source
        except Exception as e:
            print(f"NetworkError getting page source for {url}: {e}")
            return None

asyncio.run(get_source_by_playwright(url))