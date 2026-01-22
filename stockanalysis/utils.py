from bs4 import BeautifulSoup
import requests
import re

def scrape_stock_data(symbol, exchange):
    exchange = None
    url = f"https://finance.yahoo.com/quote/{symbol}/"
    # print(url)
    # Send a request and parse the HTML
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:

            soup = BeautifulSoup(response.text, "html.parser")
            current_price = soup.find("span", {"data-testid": "qsp-price"}).text
            previous_close = soup.find("fin-streamer", {"data-field": "regularMarketPreviousClose"}).text
            price_changed = soup.find("span", {"data-testid": "qsp-price-change"}).text
            percentage_changed = soup.find("span", {"data-testid": "qsp-price-change-percent"}).text
            # percentage_changed = re.sub(r"[()+]", "", percentage_changed)
            week_52_range = soup.find("fin-streamer", {"data-field": "fiftyTwoWeekRange"}).text
            week_52_low, week_52_high = week_52_range.split(' - ')
            market_cap = soup.find("fin-streamer", {"data-field": "marketCap"}).text
            pe_ratio = soup.find("fin-streamer", {"data-field": "trailingPE"}).text
            # dividend_yield = soup.find("fin-streamer", {"data-field": "Forward Dividend & Yield"}).
            dividend_yield = soup.find("span", {"title": "Forward Dividend & Yield"}).find_next("span", class_="value").text
            # dividend_yield = None

            # label = soup.find("span", {"title": "Forward Dividend & Yield"})
            # if label:
            #     value_span = label.find_next("span", class_="value")
            #     if value_span:
            #         dividend_yield = value_span.text.split("(")[1].strip(")")

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
        print(f'Error Scraping the data: {e}')
        return None

