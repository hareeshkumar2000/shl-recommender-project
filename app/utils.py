from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json
import os

def scrape_shl_assessments():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.shl.com/solutions/products/product-catalog/")
    time.sleep(5)

    cards = driver.find_elements(By.CSS_SELECTOR, '.card__text')

    assessments = []
    for card in cards:
        try:
            name = card.find_element(By.TAG_NAME, "h3").text.strip()
            link = card.find_element(By.XPATH, "..").get_attribute("href")
            assessments.append({
                "name": name,
                "url": link,
                "remote_support": "Yes",
                "adaptive_support": "Yes",
                "duration": "30-60 mins",
                "test_type": "Cognitive/Technical"
            })
        except Exception as e:
            print(f"Error: {e}")

    driver.quit()

    os.makedirs("data", exist_ok=True)
    with open("data/shl_data.json", "w") as f:
        json.dump(assessments, f, indent=2)

if __name__ == "__main__":
    scrape_shl_assessments()