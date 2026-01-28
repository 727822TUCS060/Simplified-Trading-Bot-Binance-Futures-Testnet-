import os
import logging
from binance.client import Client
from market_orders import place_market_order

# Structured Logging Setup [cite: 15, 41]
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    # Replace with environment variables for security
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"
    
    client = Client(api_key, api_secret)
    
    print("--- Binance Futures Bot ---")
    # Example usage based on submission guidelines [cite: 53]
    # In a real CLI, use argparse to handle: python src/main.py BTCUSDT BUY 0.01
    symbol = "BTCUSDT"
    side = "BUY"
    qty = 0.001
    
    print(f"Executing {side} for {symbol}...")
    place_market_order(client, symbol, side, qty)

if __name__ == "__main__":
    main()
