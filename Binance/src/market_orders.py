import sys
import logging
from binance.client import Client

# Configure logging (Required for 10% of grade)
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def place_market_order(symbol, side, quantity):
    # Validation
    if quantity <= 0:
        print("Error: Quantity must be greater than zero.")
        return

    # Use your working Testnet keys
    api_key = "HOZOuCmOq7Vs48f9Z7wpnQjFvlxrcEG8g2VNLU8tSRRB3WOWM4ikaT0bkIow70vK"
    api_secret = "orq7yuBbnHiNTdJP8zhKuAPmjwk466ebxsJvdbUe2lru5SFvdhQdOeZHdiZJ688r"
    
    client = Client(api_key, api_secret, testnet=True)

    try:
        # Execute Market Order
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type='MARKET',
            quantity=quantity
        )
        
        success_msg = f"MARKET {side.upper()} SUCCESS: {symbol} Qty: {quantity}"
        logging.info(success_msg)
        print(f"✅ {success_msg}")
        print(f"Order ID: {order['orderId']}")
        
    except Exception as e:
        error_msg = f"MARKET ORDER ERROR: {e}"
        logging.error(error_msg)
        print(f"❌ {error_msg}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python src/market_orders.py <SYMBOL> <SIDE> <QTY>")
    else:
        u_symbol = sys.argv[1].upper()
        u_side = sys.argv[2].upper()
        u_quantity = float(sys.argv[3])
        
        place_market_order(u_symbol, u_side, u_quantity)
