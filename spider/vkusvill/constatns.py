"""
File contains constants for spider
"""

URL = "https://vkusvill.ru/ajax/product_comments/from_api/comments_load_page.php?id={product_id}&rate=&brand=&page={page_number}"

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
