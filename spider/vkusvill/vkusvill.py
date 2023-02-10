import csv
import os
from collections import defaultdict

import requests
from bs4 import BeautifulSoup

from spider.vkusvill.constatns import HEADERS, REVIEW_URL, CATEGORY_URL, CATEGORY_PAGE, ITEMS_COUNT_REGEX, \
    ITEMS_ID_REGEX, MAX_REVIEW_PAGE, TITLE_TAG, MY_DIR


def save_file(title: str, reviews: list):
    file_name = os.path.join(MY_DIR, f'{title}.csv')
    with open(file_name, 'w') as file:
        write = csv.writer(file)
        write.writerows(reviews)

    print(f'SAVED {title}.csv')

def get_review(items_id: defaultdict[str, str]):
    """
    get review from item page
    """
    all_reviews = []
    with requests.Session() as session:
        session.headers = HEADERS
        for title, item_id in items_id.items():
            for page_number in range(1, 2):
                response = session.get(
                    url=REVIEW_URL.format(
                        product_id=item_id,
                        page_number=page_number,
                    ),
                    headers=HEADERS,
                )
                soup = BeautifulSoup(response.text, 'html.parser')
                raw_review = soup.find_all('div', {'class': 'Comment__text'})
                for review in raw_review:
                    all_reviews.append([review.text])
            save_file(title, all_reviews)


def _get_page_count(session) -> int:
    response = session.get(
        url=CATEGORY_PAGE,
    )
    soup = BeautifulSoup(response.text, 'html.parser')
    raw_info = soup.find('input', {'id': 'js-catalog-page-param-total-products'})
    items_count = 0
    if raw_str := ITEMS_COUNT_REGEX.search(str(raw_info)):
        items_count = round(int(raw_str.group('items_count')) / 24)
    return items_count


def get_category_items() -> defaultdict[str, str]:
    items_id = defaultdict(str)
    with requests.Session() as session:
        session.headers = HEADERS
        max_count_item = _get_page_count(session)
        for page_number in range(1, max_count_item + 1):
            response = session.get(
                url=CATEGORY_URL.format(
                    page_number=page_number,
                ),
                headers=HEADERS,
            )
            soup = BeautifulSoup(response.text, 'html.parser')
            raw_review = soup.find_all('a', {'class': ITEMS_ID_REGEX})
            raw_titles = soup.find_all('div', {'class': TITLE_TAG})
            for review, titles in zip(raw_review, raw_titles):
                items_id[titles.find('a').get('title')] = (str(review.get('data-id')))
            print(f'Get {len(items_id)} item ids count')

        return items_id


def main_crawl():
    items_id = get_category_items()
    all_review = get_review(items_id)
    print('END')


if __name__ == '__main__':
    print('START')
    main_crawl()
