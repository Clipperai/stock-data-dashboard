import pandas as pd
import yfinance as yf

from app.utils import format_error, normalize_columns


def get_stock_data(symbol: str) -> list[dict] | dict[str, str]:
    dataframe = yf.download(symbol, period="3mo", interval="1d")

    if dataframe.empty:
        return format_error("No data found. Try a valid symbol like INFY.NS")

    dataframe = normalize_columns(dataframe)
    dataframe = dataframe.reset_index()
    dataframe["Daily Returns"] = (dataframe["Close"] - dataframe["Open"]) / dataframe["Open"]
    dataframe["7MA"] = dataframe["Close"].rolling(window=7).mean()

    recent_data = dataframe.tail(30).copy()
    recent_data = recent_data.where(pd.notnull(recent_data), None)
    return recent_data.to_dict(orient="records")


def get_summary_data(symbol: str) -> dict[str, float] | dict[str, str]:
    dataframe = yf.download(symbol, period="1y", interval="1d")

    if dataframe.empty:
        return format_error("No data found")

    dataframe = normalize_columns(dataframe)
    return {
        "52_week_high": float(dataframe["High"].max()),
        "52_week_low": float(dataframe["Low"].min()),
        "average_close": float(dataframe["Close"].mean()),
    }


def compare_stocks(symbol1: str, symbol2: str) -> dict[str, float] | dict[str, str]:
    dataframe_1 = yf.download(symbol1, period="1mo")
    dataframe_2 = yf.download(symbol2, period="1mo")

    if dataframe_1.empty or dataframe_2.empty:
        return format_error("Invalid symbols")

    dataframe_1 = normalize_columns(dataframe_1)
    dataframe_2 = normalize_columns(dataframe_2)

    return_1 = ((dataframe_1["Close"].iloc[-1] - dataframe_1["Close"].iloc[0]) / dataframe_1["Close"].iloc[0]) * 100
    return_2 = ((dataframe_2["Close"].iloc[-1] - dataframe_2["Close"].iloc[0]) / dataframe_2["Close"].iloc[0]) * 100

    return {
        symbol1: round(float(return_1), 2),
        symbol2: round(float(return_2), 2),
    }
