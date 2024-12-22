This file contains the list of variables, functions, and example outputs of the "primark" brand. USing instructions from this file generate a `burberry_scraper.py` script.

- Brand name: Burberry
- Brand URL: https://us.burberry.com

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

# Examples

Here are some example inputs and outputs of the functions:

- get_pid()
    Input: 'https://us.burberry.com/check-label-cotton-t-shirt-p81048861'
    Output: 'p81048861'

- get_name()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `burberry.html`>
    Output: 'Check Label Cotton T-shirt'

- get_currency()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `burberry.html`>
    Output: '$'

- get_price()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `burberry.html`>
    Output: 390.00

- get_color_name()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `burberry.html`>
    Output: 'Chalk'

- get_colors()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `burberry.html`>
    Output: ['Chalk']

- get_sizes()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `burberry.html`>
    Output: ['XXXS', 'XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL']

- get_description()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `burberry.html`>
    Output: 'A T-shirt in cotton jersey, cut to a regular fit. Reworking the label from our signature trench.....'

- get_compositions()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `burberry.html`>
    Output: ['100% cotton']

- get_all_images_urls()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `burberry.html`>
    Output: ['https://assets.burberry.com/is/image/Burberryltd/3F147789-1371-4EE9-9651-AC94A81C3D41?$BBY_V3_SL_1$&wid=1501&hei=1500',
    'https://assets.burberry.com/is/image/Burberryltd/383142F8-D9C7-4FBC-BCCF-783EF5075DEE?$BBY_V3_SL_1$&wid=1501&hei=1500']

- get_image_url()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `burberry.html`>
    Output: 'https://assets.burberry.com/is/image/Burberryltd/3F147789-1371-4EE9-9651-AC94A81C3D41?$BBY_V3_SL_1$&wid=1501&hei=1500'