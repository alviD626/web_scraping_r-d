This file contains the list of variables, functions, and example outputs of the "primark" brand. USing instructions from this file generate a `jaded_scraper.py` script.

- Brand name: Jaded
- Brand URL: https://jadedldn.com

# Functions

Generate the following functions in the `jaded_scraper.py` script:
- get_pid()
- get_name()
- get_currency()
- get_price()
- get_price_after_discount()
- get_sizes()
- get_rating()
- get_review_count()
- get_description()
- get_details()
- get_compositions()
- get_all_images_urls()
- get_image_url()

# Examples

Here are some example inputs and outputs of the functions:

- get_pid()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: 'JWT4120'

- get_name()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: 'Rock Revival Denim Corset Top'

- get_currency()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: '£'

- get_price()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: 80

- get_price_after_discount()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: 56

- get_sizes()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: ['UK 4', 'UK 6', 'UK 8', 'UK 10', 'UK 12', 'UK 14', 'UK 16']

- get_rating()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: None

- get_review_count()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: None

- get_description()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: 'Rock Revival x Jaded London denim corset top in stretch mid-blue wash denim with branded chest pocket details and metal hardware. Fastens with a button front. Can be worn as as a matching set with the Rock Revival x Jaded London capris.....'

- get_details()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: ['Strapless corset top',
    'Stretch denim',
    'Mid blue wash',
    'Button front fastening',
    'Heavy topstitch detail throughout',
    'Branded metal hardware',
    'Co-branded chest pocket detail with diamante',
    'Black leather branded jacron label',
    'Co-ord with capris and mini shorts from collection']

- get_compositions()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: ['99% Cotton', '1% Elastane']

- get_all_images_urls()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: ['https://media.jadedldn.com//cdn/shop/files/5APRWOMENS44962.jpg',
    'https://media.jadedldn.com//cdn/shop/files/5APRWOMENS44816.jpg',
    'https://media.jadedldn.com//cdn/shop/files/5APRWOMENS44846.jpg',
    'https://media.jadedldn.com//cdn/shop/files/5APRWOMENS44922.jpg',
    'https://media.jadedldn.com//cdn/shop/files/5APRWOMENS44904.jpg']

- get_image_url()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `jaded.html`>
    Output: 'https://media.jadedldn.com//cdn/shop/files/5APRWOMENS44922.jpg'