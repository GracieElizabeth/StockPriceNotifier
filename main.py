from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import yagmail
import time
from datetime import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()
sender = os.getenv('EMAIL_SENDER')
receiver = 'fawawog1nih2@10mail.xyz'
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

def send_email(percent, stock_name, is_positive):
    subject = f"The stock {stock_name} has changed!"

    contents = f"""
    Stock: {stock_name}
    Percent Change: {percent}
    """

    yag = yagmail.SMTP(user=sender, password=os.getenv('EMAIL_PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email sent")

def get_page_info():
    driver = get_driver()
    source_code = driver.page_source
    driver.quit()

    is_positive = True
    soup = BeautifulSoup(source_code, 'html.parser')

    percent = soup.find("span", class_="stock-trend trend-grow").get_text(strip=True)
    print(f"Original value: {percent}")

    cleaned_value = percent.replace(f'{percent[0]}', '').replace('%', '')
    print(f"Cleaned value: {cleaned_value}")

    stock_name = soup.find("div", class_="stock-page-left").h1.get_text(strip=True)
    print(stock_name)

    if percent[0] == "-": is_positive = False

    return percent, stock_name, is_positive, float(cleaned_value) * 100

while True:
    now = dt.now()
    if now.minute == 45:
        percent, stock_name, is_positive, cleaned_value = get_page_info()
        if cleaned_value > 10 or cleaned_value < 10:
            send_email(percent, stock_name, is_positive)
        time.sleep(60)
    else:
        time.sleep(5)