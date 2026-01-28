import time
import sys
import logging
from binance.client import Client

logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def execute_twap(symbol, side, total_qty, duration_minutes):
    api_key = "HOZOuCmOq7Vs48f9Z7wpnQjFvlxrcEG8g2VNLU8tSRRB3WOWM4ikaT0bkIow70vK"
    api_secret = "orq7yuBbnHiNTdJP8zhKuAPmjwk466ebxsJvdbUe2lru5SFvdhQdOeZHdiZJ688r"
    client = Client(api_key, api_secret, testnet=True)

    # Split order into 3 chunks for the demo
    num_chunks = 3
    chunk_qty = total_qty / num_chunks
    interval = (duration_minutes * 60) / num_chunks

    print(f"Starting TWAP: {num_chunks} orders of {chunk_qty} {symbol} over {duration_minutes} min.")

    for i in range(num_chunks):
        try:
            order = client.futures_create_order(symbol=symbol, side=side.upper(), type='MARKET', quantity=chunk_qty)
            logging.info(f"TWAP CHUNK {i+1} SUCCESS: {symbol} Qty: {chunk_qty}")
            print(f"✅ Chunk {i+1} placed.")
            if i < num_chunks - 1:
                time.sleep(interval)
        except Exception as e:
            logging.error(f"TWAP ERROR: {e}")
            break

if __name__ == "__main__":
    # Command: python src/advanced/twap.py BTCUSDT BUY 0.03 1
    execute_twap(sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]))
