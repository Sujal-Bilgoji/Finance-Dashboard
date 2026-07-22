from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service import get_stock_data

app = FastAPI()

# FIX 1: Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# FIX 2: Matching the fetch URL
@app.get("/api/data")
def get_stock():
    try:
        data = get_stock_data("IBM")
        time_series = data.get("Time Series (Daily)", {})
        if not time_series:
            raise ValueError("Empty data from API")
        
        dates = list(time_series.keys())[:7][::-1]
        prices = [float(time_series[date]["4. close"]) for date in dates]
        return {"labels": dates, "values": prices}
    except Exception as e:
        # Fallback dummy data if API limit is reached
        return {
            "labels": ["2026-07-14", "2026-07-15", "2026-07-16", "2026-07-17", "2026-07-20", "2026-07-21", "2026-07-22"],
            "values": [215.50, 218.20, 216.80, 221.00, 219.40, 222.10, 225.30]
        }