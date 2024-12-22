This file contains the list of variables, functions, and example outputs of the "primark" brand. USing instructions from this file generate a `arne_clo_scraper.py` script.

- Brand name: Arne clo
- Brand URL: https://arneclo.com/en-us

# Functions

Generate the following functions in the `arne_clo_scraper.py` script:
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

# Examples

Here are some example inputs and outputs of the functions:

- get_pid()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `arne_clo.html`>
    Output: 'womens-towelling-revere-collar-shirt-taupe'

- get_name()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `arne_clo.html`>
    Output: 'Womens Towelling Revere Collar Shirt'

- get_currency()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `arne_clo.html`>
    Output: '$'

- get_price()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `arne_clo.html`>
    Output: 46.0

- get_color_name()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `arne_clo.html`>
    Output: 'Taupe'

- get_colors()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `arne_clo.html`>
    Output: ['ecru', 'taupe']

- get_sizes()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `arne_clo.html`>
    Output: ['XXS (6-8)','XS (8-10)','S (10-12)','M (12-14)','L (14-16)','XL (16)','XXL (18)']

- get_description()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `arne_clo.html`>
    Output: 'Model Information:Model is 5ft 7Model wears a size XXSMaterials & Care:100% cotton98% cotton.....'

- get_compositions()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `arne_clo.html`>
    Output: ['100% cotton']

- get_all_images_urls()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `arne_clo.html`>
    Output: ['https://arneclo.com/cdn/shop/files/TAUPE_TOWELINGSETS_ARNE_ECOM8406.jpg?v=1721766760',
    'https://arneclo.com/cdn/shop/files/TAUPE_TOWELINGSETS_ARNE_ECOM8239.jpg?v=1721766205',
    'https://arneclo.com/cdn/shop/files/TAUPE_TOWELINGSETS_ARNE_ECOM8185.jpg?v=1721766202',
    'https://arneclo.com/cdn/shop/files/TAUPE_TOWELINGSETS_ARNE_ECOM8225.jpg?v=1721766199',
    'https://arneclo.com/cdn/shop/files/TAUPE_TOWELINGSETS_ARNE_ECOM8332.jpg?v=1721766456',
    'https://arneclo.com/cdn/shop/files/TAUPE_TOWELINGSETS_ARNE_ECOM8268.jpg?v=1721766282']

- get_image_url()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `arne_clo.html`>
    Output: 'https://arneclo.com/cdn/shop/files/TAUPE_TOWELINGSETS_ARNE_ECOM8225.jpg?v=1721766199'