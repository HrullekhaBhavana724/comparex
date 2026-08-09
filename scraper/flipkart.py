from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_flipkart_price(product_name):

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"]
    )

    options.add_experimental_option(
        "useAutomationExtension",
        False
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.execute_script("""
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    })
    """)

    search = product_name.replace(" ", "+")

    url = f"https://www.flipkart.com/search?q={search}"

    driver.get(url)

    try:

        price = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.hZ3P6w.DeU9vF")
            )
        ).text

        price = int(
            price.replace("₹", "")
                 .replace(",", "")
                 .strip()
        )

        print("Flipkart Price:", price)

        driver.quit()

        return price

    except Exception as e:

        print("Flipkart Price Not Found")
        print(e)

        driver.save_screenshot("flipkart_error.png")

        driver.quit()

        return None


if __name__ == "__main__":

    get_flipkart_price("iPhone 16")