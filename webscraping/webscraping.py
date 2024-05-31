import time
from rich import print
from playwright.sync_api import sync_playwright


def scrapping():
    def handleJson(response):
        if "ccstore/v1/products" in response.url:
            items = response.json().get("items", [])
            for item in items:
                description = item.get("description")
                child_skus = item.get("childSKUs", [])
                if child_skus:
                    list_price = child_skus[0].get("listPrice")
                    sale_price = child_skus[0].get("salePrice")
                else:
                    list_price = None
                    sale_price = None

                print({
                    "description": description,
                    "listPrice": list_price,
                    "salePrice": sale_price
                })

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size(
            {"width": 1280, "height": 1080}
        )
        page.on("response", lambda response: handleJson(response))
        page.goto(
            "https://www.confianca.com.br/jau/c/l-ofertas/l-ofertas?Ns=product.analytics.factorQuantitySold30d|1")
        time.sleep(5)
        # page.get_by_role("paragraph").filter(has_text="Jau").click()
        page.wait_for_load_state("networkidle")

        # scroll
        # for x in range(1, 5):
        #     page.evaluee("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(2)

        browser.close()


def main():
    scrapping()


if __name__ == "__main__":
    main()
