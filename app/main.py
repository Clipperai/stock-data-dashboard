from fastapi import FastAPI
from app.data import get_stock_data, get_summary_data, compare_stocks

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Working"}

@app.get("/data/{symbol}")
def data(symbol: str):
    return get_stock_data(symbol)

@app.get("/summary/{symbol}")
def summary(symbol: str):
    return get_summary_data(symbol)

@app.get("/compare")
def compare(symbol1: str, symbol2: str):
    return compare_stocks(symbol1, symbol2)