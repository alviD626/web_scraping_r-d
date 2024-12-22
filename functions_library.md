This file contains the list of functions (to be generated) and their definitions and explanations. Also it contains the list of utils functions available in the codebase.

# Functions

Generate the following functions in the `primark_scraper.py` script:
- `get_pid(product_url: str OR source: BeautifulSoup) -> str`
    Explanation: This function usually expects a product_url and it parses the PID from the URL.
    Available utils: `extract_match`.
- `get_name(source: BeautifulSoup) -> str`
    Explanation: This function parses the product name typically from the `title` or `h1` tags.
- `get_currency(source: BeautifulSoup) -> str`
    Explanation: This function parses the currency symbol or code from the price information.
- `get_price(source: BeautifulSoup) -> float`
    Explanation: This function extracts the price before discount.
    Available utils: `extract_number`.
- `get_color_name(source: BeautifulSoup) -> str`
    Explanation: It parses the main color name.
- `get_colors(source: BeautifulSoup) -> list`
    Explanation: It returns the list of available colors.
- `get_description(source: BeautifulSoup) -> str`
    Explanation: It extracts the product description.
- `get_details(source: BeautifulSoup) -> list`
    Explanation: It extracts the list of product details.
- `get_compositions(source: BeautifulSoup) -> list`
    Explanation: It extracts the compositions as a list.
    Example Output Format: ['80% Cotton', '15% Polyester', '5% Viscode']
- `get_all_images_urls(source: BeautifulSoup) -> list`
    Explanation: It extracts all the product image URLs as a list.
- `get_image_url(source: BeautifulSoup) -> str:`
    Explanation: It selects the main image URL if not possible provide the first image URL.