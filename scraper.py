import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from config import CRYPTO_URL, TOP_COINS, HEADLESS


def create_driver():
    """Create Chrome WebDriver."""

    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Use eager loading
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.set_page_load_timeout(60)

    return driver


def scrape_top_coins():

    driver = create_driver()

    try:

        print("Opening CoinPaprika...")

        driver.get(CRYPTO_URL)

        # Wait until body is available
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        # Give JavaScript time to render
        time.sleep(8)

        print("Website loaded!")
        print("Extracting Top 10 cryptocurrencies...\n")

        body = driver.find_element(By.TAG_NAME, "body")

        text = body.text

        lines = [
            line.strip()
            for line in text.split("\n")
            if line.strip()
        ]

        # Find cryptocurrency table header
        header = [
            "#",
            "Name",
            "Price",
            "1h",
            "24h",
            "7d",
            "Volume (24h)",
            "Liquidity",
            "Market Cap"
        ]

        table_start = None

        for i in range(len(lines) - len(header)):

            if lines[i:i + len(header)] == header:

                table_start = i + len(header)

                break

        # Fallback header detection
        if table_start is None:

            for i in range(len(lines) - 3):

                if (
                    lines[i] == "#"
                    and lines[i + 1] == "Name"
                    and lines[i + 2] == "Price"
                ):

                    table_start = i + 3

                    break

        if table_start is None:

            print("Cryptocurrency table header not found!")

            print("\nPage title:", driver.title)
            print("URL:", driver.current_url)
            print("Number of lines:", len(lines))

            return []

        data = []

        i = table_start

        while len(data) < TOP_COINS:

            if i + 8 >= len(lines):
                break

            rank = lines[i]
            name = lines[i + 1]
            symbol = lines[i + 2]
            price = lines[i + 3]
            change_1h = lines[i + 4]
            change_24h = lines[i + 5]
            change_7d = lines[i + 6]
            volume = lines[i + 7]
            market_cap = lines[i + 8]

            if not rank.isdigit():

                i += 1

                continue

            data.append({
                "Rank": rank,
                "Name": name,
                "Symbol": symbol,
                "Price": price,
                "24h Change": change_24h,
                "Market Cap": market_cap
            })

            i += 9

        print("==============================================")
        print("       TOP 10 CRYPTOCURRENCIES")
        print("==============================================")

        for coin in data:

            print(
                f"{coin['Rank']}. "
                f"{coin['Name']} ({coin['Symbol']})"
            )

            print(f"   Price       : {coin['Price']}")
            print(f"   24h Change  : {coin['24h Change']}")
            print(f"   Market Cap  : {coin['Market Cap']}")

            print("----------------------------------------------")

        print(
            f"\nSuccessfully collected "
            f"{len(data)} cryptocurrencies."
        )

        return data

    except Exception as e:

        print("ERROR:", type(e).__name__)
        print("MESSAGE:", e)

        return []

    finally:

        driver.quit()


if __name__ == "__main__":

    scrape_top_coins()