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
    # Fetching IBM as default for your dashboard
    data = get_stock_data("IBM")
    time_series = data.get("Time Series (Daily)", {})
    dates = list(time_series.keys())[:7][::-1]
    prices = [float(time_series[date]["4. close"]) for date in dates]
    
    return {"labels": dates, "values": prices}