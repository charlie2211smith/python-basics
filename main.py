import yfinance as yf
from dotenv import load_dotenv
from os import getenv
from openai import OpenAI
load_dotenv()
stock = yf.Ticker("AVGO")
data = stock.history(period="1mo")
client = OpenAI(api_key=getenv("OPENAI_API_KEY"))
completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "Imagine you are a stock analyst"
                },
                {
                    "role": "user",
                    "content": f"Analyze this stock data and tell me if you see any patterns. Here is the data {data}."
                },
            ],
        )

print(completion.choices[0].message.content)




