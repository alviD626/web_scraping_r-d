This file contains the list of variables, functions, and example outputs of the "primark" brand. USing instructions from this file generate a `brandy_melville_scraper.py` script.

- Brand name: Brandy Melville
- Brand URL: https://us.brandymelville.com

# Functions

Generate the following functions in the `brandy_melville_scraper.py` script:
- get_pid()
- get_name()
- get_currency()
- get_price()
- get_color_name()
- get_colors()
- get_sizes()
- get_description()
- get_compositions()
- get_all_images_urls()
- get_image_url()
- get_manufacturing_country()

# Examples

Here are some example inputs and outputs of the functions:

- get_pid()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `brandy_melville.html`>
    Output: 'MDA110-Z087SC05V415072'

- get_name()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `brandy_melville.html`>
    Output: 'Brooklyn Hoodie'

- get_currency()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `brandy_melville.html`>
    Output: '$'

- get_price()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `brandy_melville.html`>
    Output: 42

- get_color_name()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `brandy_melville.html`>
    Output: 'Grey'

- get_colors()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `brandy_melville.html`>
    Output: ['Grey']

- get_sizes()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `brandy_melville.html`>
    Output: ['Oversized Fit']

- get_description()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `brandy_melville.html`>
    Output: 'Product Description:Soft, oversized fit hoodie with the Brooklyn Graphic printed in navy on the.....'

- get_compositions()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `brandy_melville.html`>
    Output: ['70% cotton', '30% polyester']

- get_all_images_urls()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `brandy_melville.html`>
    Output: ['https://us.brandymelville.com/cdn/shop/files/MDA110-Z087SC05V415072-01_1500x.jpg?v=1727396304',
    'https://us.brandymelville.com/cdn/shop/files/MDA110-Z087SC05V415072-03_1500x.jpg?v=1727396336',
    'https://us.brandymelville.com/cdn/shop/files/MDA110-Z087SC05V415072-04_1500x.jpg?v=1727396258',
    'https://us.brandymelville.com/cdn/shop/files/MDA110-Z087SC05V415072-02_1500x.jpg?v=1727396444']

- get_image_url()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `brandy_melville.html`>
    Output: 'https://us.brandymelville.com/cdn/shop/files/MDA110-Z087SC05V415072-01_1500x.jpg?v=1727396304'

- get_manufacturing_country()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `brandy_melville.html`>
    Output: 'China'