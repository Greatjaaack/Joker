import asyncio
import json

from playwright.sync_api import sync_playwright

MOSCOW = "https://yandex.ru/maps/213/moscow/?ll=37.617700%2C55.755863&z=10"
REVIEWS_ISKRA = "https://yandex.ru/maps/org/iskra/1161458972/reviews/?ll=37.584460%2C55.805528&z=16"


def main():
    # TODO: вынеси в отдельный класс

    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(REVIEWS_ISKRA)

        # TODO: вынеси в одтельный класс
        page.locator(".business-reviews-card-view__ranking").locator('"По умолчанию"').click()
        page.locator(".rating-ranking-view__popup").locator('"По новизне"').click()

        try:
            raw_review = json.loads(
                page.locator('.state-view').inner_text(),
            )

            # TODO: собери всё по этому пути -> stack►0►results►items►0►reviewResults
        except Exception as err_msg:
            print(err_msg)

        finally:
            print('><')

        # other actions....
        asyncio.sleep(60)
        browser.close()


if __name__ == '__main__':
    print("START")
    main()
    # asyncio.run(main())
