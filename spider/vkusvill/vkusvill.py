import time

import requests
from bs4 import BeautifulSoup

from spider.vkusvill.constatns import URL, HEADERS


def make_request() -> None:
    """
    Main func to create request
    """
    with requests.Session() as session:
        session.headers = HEADERS
        get_review(session)


def get_review(session):
    """
    get review from item page
    """
    for page_nuber in range(1, 400):
        response = session.get(
            url=URL.format(
                product_id='61780',
                page_number=page_nuber,
            ),

            headers=HEADERS,
        )
        soup = BeautifulSoup(response.text, 'html.parser')
        raw_review = soup.find_all('div', {'class': 'Comment__text'})
        for i in raw_review:
            print(i.text)
        time.sleep(1)


if __name__ == '__main__':
    make_request()
