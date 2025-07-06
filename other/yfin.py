import yfinance as yf
df = yf.download("AAPL", start="2023-01-01", end="2024-01-01")
print(df[['Close', 'Volume']])