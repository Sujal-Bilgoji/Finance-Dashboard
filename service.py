import requests

API_KEY = "3IQJZXOGU05X5VX3"
BASE_URL = "https://www.alphavantage.co/query"

def get_stock_data(symbol="IBM"):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()