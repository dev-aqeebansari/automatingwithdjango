from bs4 import BeautifulSoup
import requests
import re

def scrape_stock_data(symbol, exchange):
    symbol = symbol.upper()
    if exchange == 'BSE':
        url = f"https://finance.yahoo.com/quote/{symbol}.BO/"
    elif exchange == 'NSE':
        url = f"https://finance.yahoo.com/quote/{symbol}.NS/"
    else:
        url = f"https://finance.yahoo.com/quote/{symbol}/"

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/"
    }
    # Send a request and parse the HTML
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            current_price = soup.find("span", {"data-testid": "qsp-price"}).text
            previous_close = soup.find("fin-streamer", {"data-field": "regularMarketPreviousClose"}).text
            price_changed = soup.find("span", {"data-testid": "qsp-price-change"}).text
            percentage_changed = soup.find("span", {"data-testid": "qsp-price-change-percent"}).text
            week_52_range = soup.find("fin-streamer", {"data-field": "fiftyTwoWeekRange"}).text
            week_52_low, week_52_high = week_52_range.split(' - ')
            market_cap = soup.find("fin-streamer", {"data-field": "marketCap"}).text
            pe_ratio = soup.find("fin-streamer", {"data-field": "trailingPE"}).text
            dividend_yield = soup.find("span", {"title": "Forward Dividend & Yield"}).find_next("span", class_="value").text

            stock_response = {
                "current_price" : current_price,
                "previous_close" : previous_close,
                "price_changed" : price_changed,
                "percentage_changed" : percentage_changed,
                "week_52_range": week_52_range,
                "week_52_low": week_52_low,
                "week_52_high": week_52_high,
                "market_cap": market_cap,
                "pe_ratio" : pe_ratio,
                "dividend_yield" : dividend_yield
            }
            return stock_response

    except Exception as e:
        return None

