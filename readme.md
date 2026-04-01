# 📊 Stock Data Intelligence Dashboard

## 🚀 Overview
A mini financial data platform that fetches real-time stock data, processes it, and provides insights using REST APIs.

---

## ⚙️ Tech Stack
- Python
- FastAPI
- Pandas
- yFinance

---

## 📡 API Endpoints

### 1. Get Stock Data
`/data/{symbol}`  
Returns last 30 days data with:
- Daily Returns
- 7-day Moving Average

---

### 2. Get Summary
`/summary/{symbol}`  
Returns:
- 52-week high
- 52-week low
- Average closing price

---

### 3. Compare Stocks
`/compare?symbol1=INFY.NS&symbol2=TCS.NS`  
Returns performance comparison

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload