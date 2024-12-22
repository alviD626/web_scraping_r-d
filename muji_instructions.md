This file contains the list of variables, functions, and example outputs of the "primark" brand. USing instructions from this file generate a `muji_scraper.py` script.

- Brand name: Muji
- Brand URL: https://www.muji.us

# Functions

Generate the following functions in the `burberry_scraper.py` script:
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
    Input: 'https://www.muji.us/collections/womens-tops/products/womens-washable-high-gauge-high-neck-sweater-ba1oy24a'
    Output: 'ba1oy24a'

- get_name()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `muji.html`>
    Output: 'Women's Washable High-Gauge High Neck Sweater'

- get_currency()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `muji.html`>
    Output: '$'

- get_price()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `muji.html`>
    Output: 49.90

- get_color_name()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `muji.html`>
    Output: 'Off White'

- get_colors()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `muji.html`>
    Output: ['Dark Green', 'Black', 'Dark Gray', 'Off White', 'Oatmeal']

- get_sizes()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `muji.html`>
    Output: ['XS', 'S', 'M', 'L', 'XL', 'XXL']

- get_description()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `muji.html`>
    Output: 'A classic high neck sweater made of warm wool, with an extra soft texture......'

- get_compositions()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `muji.html`>
    Output: ['100% Wool']

- get_all_images_urls()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `muji.html`>
    Output: ['www.muji.us/cdn/shop/files/4550584104978_04_org_2000x2000.jpg?v=1729712460',
    'www.muji.us/cdn/shop/files/4550584104992_02_org_2000x2000.jpg?v=1724340814',
    'www.muji.us/cdn/shop/files/4550584104879_02_org_2000x2000.jpg?v=1724340759',
    'www.muji.us/cdn/shop/files/4550584104633_03_org_2000x2000.jpg?v=1724953542',
    'www.muji.us/cdn/shop/files/4550584104879_05_org_2000x2000.jpg?v=1724340747',
    'www.muji.us/cdn/shop/files/4550584104992_03_org_2000x2000.jpg?v=1724340814',
    'www.muji.us/cdn/shop/files/4550584104695_02_org_2000x2000.jpg?v=1724953551',
    'www.muji.us/cdn/shop/files/4550584104879_org_dfb85973-fc65-4730-b27e-680a47dadeb6_2000x2000.jpg?v=1724340747',
    'www.muji.us/cdn/shop/files/4550584104756_04_org_2000x2000.jpg?v=1724953572',
    'www.muji.us/cdn/shop/files/4550584104633_org_2000x2000.jpg?v=1724953538',
    'www.muji.us/cdn/shop/files/4550584104695_org_2000x2000.jpg?v=1724953546',
    'www.muji.us/cdn/shop/files/4550584105043_01_org_2000x2000.jpg?v=1729712476',
    'www.muji.us/cdn/shop/files/4550584104817_01_org_2000x2000.jpg?v=1724953592',
    'www.muji.us/cdn/shop/files/4550584104992_05_org_2000x2000.jpg?v=1724340802',
    'www.muji.us/cdn/shop/files/4550584104978_org_2000x2000.jpg?v=1729712454',
    'www.muji.us/cdn/shop/files/4550584105043_05_org_2000x2000.jpg?v=1729712469',
    'www.muji.us/cdn/shop/files/4550584104978_06_org_2000x2000.jpg?v=1729712460',
    'www.muji.us/cdn/shop/files/4550584104879_01_org_2000x2000.jpg?v=1724340758',
    'www.muji.us/cdn/shop/files/4550584104756_02_org_2000x2000.jpg?v=1724953572',
    'www.muji.us/cdn/shop/files/4550584104879_org_2000x2000.jpg?v=1724340741',
    'www.muji.us/cdn/shop/files/4550584104879_03_org_2000x2000.jpg?v=1724340758',
    'www.muji.us/cdn/shop/files/4550584104633_06_org_2000x2000.jpg?v=1724953542',
    'www.muji.us/cdn/shop/files/4550584104695_03_org_2000x2000.jpg?v=1724953551',
    'www.muji.us/cdn/shop/files/4550584104817_04_org_2000x2000.jpg?v=1724953592',
    'www.muji.us/cdn/shop/files/4550584104756_01_org_2000x2000.jpg?v=1724953571',
    'www.muji.us/cdn/shop/files/4550584104633_01_org_2000x2000.jpg?v=1724953542',
    'www.muji.us/cdn/shop/files/4550584104817_02_org_2000x2000.jpg?v=1724953592',
    'www.muji.us/cdn/shop/files/4550584105043_04_org_2000x2000.jpg?v=1729712476',
    'www.muji.us/cdn/shop/files/4550584105043_org_2000x2000.jpg?v=1729712469',
    'www.muji.us/cdn/shop/files/4550584104756_03_org_2000x2000.jpg?v=1724953572',
    'www.muji.us/cdn/shop/files/4550584104817_06_org_2000x2000.jpg?v=1724953592',
    'www.muji.us/cdn/shop/files/4550584104978_01_org_2000x2000.jpg?v=1729712461',
    'www.muji.us/cdn/shop/files/4550584104879_04_org_2000x2000.jpg?v=1724340758',
    'www.muji.us/cdn/shop/files/4550584104992_org_2000x2000.jpg?v=1724340802',
    'www.muji.us/cdn/shop/files/4550584105043_06_org_2000x2000.jpg?v=1729712476',
    'www.muji.us/cdn/shop/files/4550584104879_06_org_2000x2000.jpg?v=1724340759',
    'www.muji.us/cdn/shop/files/4550584104817_05_org_2000x2000.jpg?v=1724953585',
    'www.muji.us/cdn/shop/files/4550584104695_05_org_2000x2000.jpg?v=1724953546',
    'www.muji.us/cdn/shop/files/4550584104756_05_org_2000x2000.jpg?v=1724953565',
    'www.muji.us/cdn/shop/files/4550584104817_org_2000x2000.jpg?v=1724953585',
    'www.muji.us/cdn/shop/files/4550584104695_01_org_2000x2000.jpg?v=1724953551',
    'www.muji.us/cdn/shop/files/4550584104633_02_org_2000x2000.jpg?v=1724953542',
    'www.muji.us/cdn/shop/files/4550584104992_04_org_2000x2000.jpg?v=1724340814',
    'www.muji.us/cdn/shop/files/4550584104992_06_org_2000x2000.jpg?v=1724340814',
    'www.muji.us/cdn/shop/files/4550584104633_04_org_2000x2000.jpg?v=1724953542',
    'www.muji.us/cdn/shop/files/4550584105043_02_org_2000x2000.jpg?v=1729712476',
    'www.muji.us/cdn/shop/files/4550584104756_06_org_2000x2000.jpg?v=1724953572',
    'www.muji.us/cdn/shop/files/4550584104817_03_org_2000x2000.jpg?v=1724953592',
    'www.muji.us/cdn/shop/files/4550584104978_03_org_2000x2000.jpg?v=1729712460',
    'www.muji.us/cdn/shop/files/4550584105043_03_org_2000x2000.jpg?v=1729712476',
    'www.muji.us/cdn/shop/files/4550584104756_org_2000x2000.jpg?v=1724953565',
    'www.muji.us/cdn/shop/files/4550584104978_05_org_2000x2000.jpg?v=1729712452',
    'www.muji.us/cdn/shop/files/4550584104992_01_org_2000x2000.jpg?v=1724340814',
    'www.muji.us/cdn/shop/files/4550584104695_04_org_2000x2000.jpg?v=1724953551',
    'www.muji.us/cdn/shop/files/4550584104695_06_org_2000x2000.jpg?v=1724953551',
    'www.muji.us/cdn/shop/files/4550584104633_05_org_2000x2000.jpg?v=1724953538',
    'www.muji.us/cdn/shop/files/4550584104978_02_org_2000x2000.jpg?v=1729712460']

- get_image_url()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `muji.html`>
    Output: 'www.muji.us/cdn/shop/files/4550584104879_org_2000x2000.jpg?v=1724340741'

- get_manufacturing_country()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `muji.html`>
    Output: 'Thailand'