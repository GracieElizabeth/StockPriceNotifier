# StockPriceNotifier
# Stock Price Monitoring Script

This Python script monitors the stock price for a specific stock on the Zagreb Stock Exchange website and sends an email notification when the stock price changes by more than 10%. It uses Selenium for web scraping, BeautifulSoup for parsing HTML, Yagmail for sending emails, and Python's built-in modules for scheduling and environment variable management.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Setup](#setup)

## Getting Started

These instructions will help you set up and run the stock price monitoring script on your local machine.

### Prerequisites

Before you begin, you need to have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Selenium](https://pypi.org/project/selenium/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [Yagmail](https://pypi.org/project/yagmail/)
- [Dotenv](https://pypi.org/project/python-dotenv/)
- [Google Chrome](https://www.google.com/chrome/) and [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### Setup

1. Clone the repository or download the script files.

2. Install the required Python packages using pip:
   ```bash
   pip install selenium beautifulsoup4 yagmail python-dotenv
