from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = 'https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6'

def get_driver():
    # Set options to make browsing easier
    chrome_settings = webdriver.ChromeOptions()
    chrome_settings.add_argument("disable-infobars") # Disable the info bar if website has it
    chrome_settings.add_argument("start-maximized") # Start browser as maximized
    chrome_settings.add_argument("disable-dev-shm-usage") # Disabled devshm for Linux
    chrome_settings.add_argument("no-sandbox") # Disable sandboxing mode
    chrome_settings.add_argument("headless")  # Run in headless mode
    # Enable script to access browser
    chrome_settings.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_settings.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=chrome_settings) # Initialize driver with above options
    driver.get(url)
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "stock-trend"))
    )
    return driver

def main():
    driver = get_driver()
    source_code = driver.page_source
    driver.quit()

    soup = BeautifulSoup(source_code, 'html.parser')

    percent = soup.find("span", class_="stock-trend trend-grow").get_text(strip=True)
    print(f"Original value: {percent}")

    cleaned_value = percent.replace(f'{percent[0]}', '').replace('%', '')
    print(f"Cleaned value: {cleaned_value}")

main()
