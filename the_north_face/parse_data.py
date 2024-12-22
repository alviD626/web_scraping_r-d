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

url = "https://www.thenorthface.com/en-us/mens/mens-tops/mens-hoodies-and-sweatshirts-c224211/mens-evolution-crew-pNF0A86WA?color=GAZ"

# mens
# best seller
# url = "https://www.thenorthface.com/en-us/mens/mens-jackets-and-vests/mens-rainwear-c299284/mens-antora-novelty-rain-jacket-pNF0A7QF3?color=JK3"
# url = "https://www.thenorthface.com/en-us/mens/mens-tops/mens-hoodies-and-sweatshirts-c224211/mens-axys-hoodie-pNF0A86W4?color=3X4"
# jackets & vests
# url = "https://www.thenorthface.com/en-us/mens/collections/thermoball-c300772/mens-thermoball-eco-jacket-2.0-pNF0A5GLL?color=JK3" # image problem"
# url = "https://www.thenorthface.com/en-us/mens/mens-fleece/mens-fleece-full-zip-c829791/mens-gordon-lyons-full-zip-vest-pNF0A5GL3?color=DYY"
# mens fleece
# url = "https://www.thenorthface.com/en-us/mens/mens-fleece/mens-fleece-full-zip-c829791/mens-canyonlands-vest-pNF0A7UJ9?color=HKW"
# url = "https://www.thenorthface.com/en-us/mens/mens-fleece/mens-fleece-pullover-c829794/mens-canyonlands-1-2-zip-pNF0A5G9W?color=DYY"
# mens bottom
# url = "https://www.thenorthface.com/en-us/mens/mens-bottoms-c211704/mens-wander-shorts-2.0-pNF0A86R6?color=0UZ"
# url = "https://www.thenorthface.com/en-us/mens/mens-bottoms/mens-pants-c224219/mens-box-nse-joggers-pNF0A7UOA?color=MPF"


# womens
# best seller
# url = "https://www.thenorthface.com/en-us/womens/womens-tops/womens-hoodies-and-sweatshirts-c224264/womens-fine-alpine-hoodie-pNF0A8AWF?color=1I4"
# Jackets & vests
# url = "https://www.thenorthface.com/en-us/womens/womens-jackets-and-vests/womens-vests-c299280/womens-1996-retro-nuptse-vest-pNF0A3XEP?color=OAC"
# womens fleece
# url = "https://www.thenorthface.com/en-us/womens/womens-plus-sizing-c290144/womens-plus-denali-jacket-pNF0A7WMT?color=V6V"
# womens top
# url = "https://www.thenorthface.com/en-us/womens/womens-tops/womens-t-shirts-c213341/womens-short-sleeve-fine-alpine-tee-pNF0A8AWE?color=PJO"
# bottom
# url = "https://www.thenorthface.com/en-us/womens/womens-bottoms/womens-shorts-c224274/womens-tnf-easy-wind-shorts-pNF0A8712?color=QEO"
# url = "https://www.thenorthface.com/en-us/womens/womens-plus-sizing-c290144/womens-plus-bridgeway-ankle-pants-pNF0A7UM4?color=LK5"


# kids
# best seller
# url = "https://www.thenorthface.com/en-us/kids/featured/kids-rainwear-c518774/kids-antora-rain-jacket-pNF0A7ZZP?color=PIN"
# girls apparel
# url = "https://www.thenorthface.com/en-us/kids/featured/kids-rainwear-c518774/girls-warm-antora-rain-jacket-pNF0A873R?color=LK6"
# url = "https://www.thenorthface.com/en-us/womens/womens-jackets-and-vests/womens-softshells-c299274/womens-shelbe-raschel-hoodie-pNF0A84JJ?color=JK3"
# boys apparel
# url = "https://www.thenorthface.com/en-us/kids/boys-apparel/boys-jackets-and-vest-c211736/boys-antora-rain-jacket-pNF0A8A48?color=D6S"
# url = "https://www.thenorthface.com/en-us/kids/boys-apparel-c211735/boys-never-stop-shorts-pNF0A86U4?color=DYY"
# little kids apparel
# url = "https://www.thenorthface.com/en-us/kids/featured/shop-all-kids-jackets-c730283/kids-1996-retro-nuptse-jacket-pNF0A82TS?color=VIK"
# # baby
# url = "https://www.thenorthface.com/en-us/kids/baby-0-24m-c226751/baby-denali-one-piece-set-pNF0A7UMF?color=I0D"




source = asyncio.get_event_loop().run_until_complete(get_source_by_playwright(url))



# name
def p_name(source):
    name = source.find("div",class_="vf-heading product__heading").find('h1').text.strip()
    print(f"Name: {name}\n")
    return name
p_name(source)

# currecny
def p_currecny(source):
    currency = source.find('div', class_='vf-product-price').find("span").text.strip()[0]
    print(f"Currency: {currency}\n")
    return currency
p_currecny(source)

# price
def p_price(source):
    init_price = source.find('div', class_='vf-product-price').find("span",class_="vf-text vf-text--sm--text-align vf-text--md--text-align vf-text--lg--text-align vf-price--regular")
    if init_price is None:
        price = source.find('div', class_='vf-product-price').find("span",class_="vf-price").find("del").get_text(strip=True).replace("$","")
        print(f"Price: {price}\n")
        return price
    else:
        price = init_price.get_text(strip=True).replace("$","")
        print(f"Price: {price}\n")
        return price
p_price(source)



# discount_price
def discount_price(source):
    init_price = source.find('div', class_='vf-product-price').find("span",class_="vf-text vf-text--sm--text-align vf-text--md--text-align vf-text--lg--text-align vf-price--regular")
    if init_price is None:
        discount_price = source.find('div', class_='vf-product-price').find("span",class_="vf-price").find("ins").get_text(strip=True).replace("$","")
        print(f"Discount_Price: {discount_price}\n")
        return discount_price
    else:
        return ""
discount_price(source)



# colors
def p_colors(source):
    colors = source.find("div",class_="color-swatch").find("div",class_="color-swatch__wrapper color-swatch__wrapper--show-all").find_all("button")
    all_colors = []
    for color in colors:
        new_colors = color["aria-label"]
        all_colors.append(new_colors)
    print(f"Colors: {all_colors}\n")
    return all_colors
p_colors(source)


# color
def color_name(source):
    color_name = source.find("div",class_="color-swatch").find("div",class_="color-swatch__wrapper color-swatch__wrapper--show-all").find("button")["aria-label"]
    print(f"Main_color: {color_name}\n")
    return color_name
color_name(source)



# images
def p_images(source):
    images = source.find("div",class_="image-grid").find("ul").find_all("li")
    all_images = []
    for image in images:
        new_images = image.find("button")["data-image-lr"].split("url")[-1].replace("(","").replace(")","").replace("'","")
        all_images.append(new_images)
    print(f"All Images: {all_images}\n")
    return all_images
p_images(source)



# main image
def main_image(source):
    image = source.find("div",class_="image-grid").find("ul").find("li").find("button")["data-image-lr"].split("url")[-1].replace("(","").replace(")","").replace("'","")
    print(f"Main_image: {image}\n")
    return image
main_image(source)


# description 
def description(source):
    description = source.find("div",class_="vf-product-details__description").text.strip()
    print(f"Description: {description}\n")
    return description
description(source)


# details
def details(source):
    all_details = source.find("div",id = "tab-panel-name-details-content").find("div",class_="vf-product-details__productDetails")
    # Initialize an empty list to store the details
    details_list = []
    
    # Iterate over all div elements inside the product details container
    for detail in all_details.find_all("div", recursive=False):
        # Find the title and value divs
        title = detail.find("div", class_="vf-details-title").get_text(strip=True)
        value = detail.find("div", class_="vf-details-title").find_next_sibling("div").get_text(strip=True)
        # Append the formatted string to the list
        details_list.append(f"{title} {value}")
    print(f"All_Details: {details_list}\n")
    return details_list
details(source)


# id 
def p_id(source):
    p_id = source.find("div", id = "tab-panel-name-details-content").find("div",class_="vf-product-details__productDetails").find_all("div")[0].find_all("div")[-1].text.strip()
    print(f"Id: {p_id}\n")
    return p_id
p_id(source)



# sizes
def sizes(source):
    sizes = source.find("div", id = "tab-panel-name-details-content").find("div",class_="vf-product-details__productDetails")
    sizes_div = sizes.find_all("div", class_="vf-details-title")
    
    for title in sizes_div:
        if title.text.strip() == "Sizes:":
            size_value = title.find_next_sibling("div").text.strip().split(", ")
            print(f"Size: {size_value}\n")
            return size_value
    print(None)
    return None
sizes(source)

import re
# composition 
def composition(source):
    composition = source.find("div", id = "tab-panel-name-details-content").find("div",class_="vf-product-details__productDetails")
    composition_div = composition.find_all("div", class_="vf-details-title")
    
    titles_to_check = [
        "Sizes:", "Body:", "Heather Body:", "Body And Overlay:", 
        "Fabric:", "I0F, I0H, I0V Outer Body:", "Heather:"
    ]

    for title in composition_div:
        if title.text.strip() in titles_to_check:
            composition_value = title.find_next_sibling("div").text.strip()
            # composition_list = [new_composition.strip() for new_composition in composition_value.split(',')]

            # composition_list = composition_value
            pattern = r'(\d+% [a-zA-Z\s]+)'
            matches = re.findall(pattern, composition_value)
            # If there are matches, return them as a list
            if matches:
                print(f"Composition: {matches}\n")
                return matches
            else:
                # If no percentages, look for cases like '100% recycled polyester'
                pattern_no_percentage = r'(100% [a-zA-Z\s]+)'
                matches_no_percentage = re.findall(pattern_no_percentage, composition_value)
                if matches_no_percentage:
                    print(f"Composition: {matches_no_percentage}\n")
                    return matches_no_percentage
                
            # Return an empty list if no compositions are found
            return []
            # print(composition_list)
            # return composition_list
    # print("")
    # return ""
composition(source)