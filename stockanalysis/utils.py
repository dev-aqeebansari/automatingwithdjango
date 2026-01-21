from bs4 import BeautifulSoup
import requests

def scrape_stock_data(symbol, exchange):
    print("In the scrape function")

    exchange = exchange.upper()
    if exchange == "NSE":
        yahoo_symbol = f"{symbol}.NS"
    elif exchange == "BSE":
        yahoo_symbol = f"{symbol}.BO"
    else:
        yahoo_symbol = symbol
    
    print(yahoo_symbol)
    
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{yahoo_symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(data)
            current_price = data['chart']['result'][0]["meta"]["regularMarketPrice"]
            previous_close = data['chart']['result'][0]["meta"]["chartPreviousClose"]
            print(current_price, "  ", previous_close )

            stock_response = {
                'current_price' : current_price,
                'previous_close': previous_close,
            }
            return stock_response
        else:
            return f'Error getting the data for symbol'
    except Exception as e:
        print(f'Error getting  the data: {e}')
        return None