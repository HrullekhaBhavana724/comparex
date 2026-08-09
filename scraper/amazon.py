import sqlite3
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_amazon_price(product_name):

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    search = product_name.replace(" ", "+")

    driver.get(f"https://www.amazon.in/s?k={search}")

    time.sleep(5)

    try:
        price = driver.find_element(
            By.CLASS_NAME,
            "a-price-whole"
        ).text

        driver.quit()

        return int(price.replace(",", ""))

    except:

        driver.quit()

        return None


def update_database():

    price = get_amazon_price("iPhone 16")

    if price is None:
        print("Amazon price not found")
        return

    conn = sqlite3.connect("comparex.db")

    cur = conn.cursor()

    cur.execute("""
        UPDATE prices
        SET price=?
        WHERE product_id=5
        AND LOWER(store)='amazon'
    """, (price,))

    conn.commit()

    conn.close()

    print("Database Updated!")
    print("Amazon Price:", price)


if __name__ == "__main__":

    update_database()