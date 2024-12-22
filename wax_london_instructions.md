This file contains the list of variables, functions, and example outputs of the "primark" brand. USing instructions from this file generate a `wax_london_scraper.py` script.

- Brand name: Wax London
- Brand URL: https://waxlondon.com

# Functions

Generate the following functions in the `wax_london_scraper.py` script:
- get_pid()
- get_name()
- get_currency()
- get_price()
- get_sizes()
- get_description()
- get_details()
- get_compositions()
- get_all_images_urls()
- get_image_url()
- get_manufacturing_country()

# Examples

Here are some example inputs and outputs of the functions:

- get_pid()
    Input: 'https://waxlondon.com/collections/polos/products/atwood-blue-textured-organic-cotton-polo-shirt'
    Output: 'atwood-blue-textured-organic-cotton-polo-shirt'

- get_name()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `wax_london.html`>
    Output: 'Atwood - Blue Textured Organic Cotton Polo Shirt'

- get_currency()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `wax_london.html`>
    Output: '£'

- get_price()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `wax_london.html`>
    Output: 55.0

- get_sizes()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `wax_london.html`>
    Output: ['XS', 'S', 'M', 'L', 'XL', 'XXL']

- get_description()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `wax_london.html`>
    Output: 'Introducing our Atwood Polo.It is designed for a more relaxed fit than the Naples and.....'

- get_details()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `wax_london.html`>
    Output: ['Textured Blue',
    'Made In Bangladesh',
    '100% Organic Cotton',
    'Wash at 40°C',
    'Wash with Similar Colours',
    'Wash Inside Out',
    'Dry Flat',
    'Reshape Whilst Damp',
    'Do Not Bleach',
    'Do Not Tumble Dry',
    'Warm Iron On Reverse',
    'Do Not Dry Clean']

- get_compositions()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `wax_london.html`>
    Output: ['100% Organic Cotton']

- get_all_images_urls()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `wax_london.html`>
    Output: ['https://waxlondon.com/cdn/shop/files/atwood-blue-textured-organic-cotton-polo-shirt_800x.jpg?v=1726219723',
    'https://waxlondon.com/cdn/shop/files/atwood-blue-textured-organic-cotton-polo-shirt-2_800x.jpg?v=1726219733',
    'https://waxlondon.com/cdn/shop/files/atwood-blue-textured-organic-cotton-polo-shirt-3_800x.jpg?v=1726219742',
    'https://waxlondon.com/cdn/shop/files/atwood-blue-textured-organic-cotton-polo-shirt-4_800x.jpg?v=1726219750',
    'https://waxlondon.com/cdn/shop/files/atwood-blue-textured-organic-cotton-polo-shirt-5_800x.jpg?v=1726219758',
    'https://waxlondon.com/cdn/shop/files/atwood-blue-textured-organic-cotton-polo-shirt-6_800x.jpg?v=1726219765',
    'https://waxlondon.com/cdn/shop/files/atwood-blue-textured-organic-cotton-polo-shirt-7_800x.jpg?v=1726219773',
    'https://waxlondon.com/cdn/shop/files/atwood-blue-textured-organic-cotton-polo-shirt-8_800x.jpg?v=1726219781',
    'https://waxlondon.com/cdn/shop/files/atwood-blue-textured-organic-cotton-polo-shirt-9_800x.jpg?v=1726219789',
    'https://waxlondon.com/cdn/shop/files/atwood-blue-textured-organic-cotton-polo-shirt-10_800x.jpg?v=1726219797']

- get_image_url()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `wax_london.html`>
    Output: 'https://waxlondon.com/cdn/shop/files/atwood-blue-textured-organic-cotton-polo-shirt_800x.jpg?v=1726219723'

- get_manufacturing_country()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `wax_london.html`>
    Output: 'Bangladesh'