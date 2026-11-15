import yfinance as yf
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.client import TradingClient
from dotenv import load_dotenv
from os import getenv
from openai import OpenAI
from ai.prompts import stock_analysis_prompt

load_dotenv()
stock = yf.Ticker("AVGO")
data = stock.history(period="1mo")
client = OpenAI(api_key=getenv("OPENAI_API_KEY"))
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Imagine you are a stock analyst"},
        {"role": "user", "content": stock_analysis_prompt(data)},
    ],
)

print(completion.choices[0].message.content)
trading_client = TradingClient(
    getenv("ALPACA_API_KEY"), getenv("ALPACA_SECRET"), paper=True
)
account = trading_client.get_account()
print("Account status:", account.status)
print("Buying power:", account.buying_power)
print("Portfolio value:", account.portfolio_value)
order = MarketOrderRequest(
    symbol="AVGO", qty=1, side=OrderSide.SELL, time_in_force=TimeInForce.DAY
)
response = trading_client.submit_order(order)
