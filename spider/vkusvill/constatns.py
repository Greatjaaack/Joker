"""
File contains constants for spider
"""
import re

REVIEW_URL = "https://vkusvill.ru/ajax/product_comments/from_api/comments_load_page.php?id={product_id}&rate=&brand=&page={page_number}"
CATEGORY_URL = "https://vkusvill.ru/goods/goryachaya-eda/?PAGEN_1={page_number}"
CATEGORY_PAGE = "https://vkusvill.ru/goods/goryachaya-eda/"

HEADERS = {
    'Sec-Ch-Ua': '"Chromium";v="109", "Not_A Brand";v="99"',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Origin': 'https://vkusvill.ru',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://vkusvill.ru/goods/azu-iz-govyadiny-s-grechkoy-61780.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
}


# CONST
MAX_REVIEW_PAGE = 6
TITLE_TAG = 'ProductCard__content'

MY_DIR = '/Users/Arslan/Desktop/Joker/saved_files/'


# REGEX
ITEMS_COUNT_REGEX = re.compile(r'value=\"(?P<items_count>\d*)\"')
ITEMS_ID_REGEX = re.compile(r".*ProductCard__QuickView btn_text _desktop-sm b500 js-product-quickview.*")
REVIEWS_COUNT = re.compile(r"(?P<reviews_count>\d+)")