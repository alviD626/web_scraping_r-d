This file contains the list of variables, and example inputs and outputs of the functions used in the "primark" brand. USing instructions from this file generate a `primark_scraper.py` script.

- Brand name: Primark
- Brand URL: https://www.primark.com

# Examples

Here are some example inputs and outputs of the functions:

- get_pid()
    Input: 'https://www.primark.com/en-us/p/pointelle-thermal-top-black-991110651804'
    Output: '991110651804'

- get_name()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `primark.html`>
    Output: 'Pointelle Thermal Top'

- get_currency()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `primark.html`>
    Output: '$'

- get_price()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `primark.html`>
    Output: 9.00

- get_color_name()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `primark.html`>
    Output: 'Black'

- get_colors()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `primark.html`>
    Output: ['Black']

- get_description()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `primark.html`>
    Output: 'A long sleeve thermal top with a heart pointelle texture....'

- get_details()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `primark.html`>
    Output: ['Tops and T-Shirts', 'Neckline: Scoop', 'Fit: Regular', 'Sleeve Length: Full Length','Model Size: S', 'Material: 65% Polyester 35% Viscose', 'Fire Safety: WARNING! Keep away from fire']

- get_compositions()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `primark.html`>
    Output: ['65% Polyester', '35% Viscose']

- get_all_images_urls()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `primark.html`>
    Output: ['https://cdn.media.amplience.net/i/primark/991110651804_01', 'https://cdn.media.amplience.net/i/primark/991110651804_02', 'https://cdn.media.amplience.net/i/primark/991110651804_03', 'https://cdn.media.amplience.net/i/primark/991110651804_04', 'https://cdn.media.amplience.net/i/primark/991110651804_05', 'https://cdn.media.amplience.net/i/primark/991110651804_06']

- get_image_url()
    Input: <BeautifulSoup Parsed Object of the HTML Source Code of `primark.html`>
    Output: 'https://cdn.media.amplience.net/i/primark/991110651804_01'
