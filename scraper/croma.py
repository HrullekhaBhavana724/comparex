from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def get_croma_price(product_name):

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    search = product_name.replace(" ", "%20")

    url = f"https://www.croma.com/search/?text={search}"

    driver.get(url)

    try:

        price = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "span.amount.plp-srp-new-amount"
                )
            )
        ).text

        price = int(
            price.replace("₹", "")
                 .replace(",", "")
                 .strip()
        )

        print("Croma Price:", price)

        driver.quit()

        return price

    except Exception as e:

        print("Croma Price Not Found")
        print(e)
        try:
            driver.save_screenshot("croma_error.png")
        except:
            pass
        try:
            driver.quit()
        except:
            pass
        return None


if __name__ == "__main__":

    get_croma_price("iPhone 16")