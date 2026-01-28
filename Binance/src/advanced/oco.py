def place_futures_oco(client, symbol, side, quantity, tp_price, sl_price):
    """
    Simulates OCO by placing a Take Profit and a Stop Loss market order[cite: 10].
    Note: In Futures, these are often handled as separate 'STOP_MARKET' and 'TAKE_PROFIT_MARKET' orders.
    """
    try:
        orders = []
        # Take Profit
        tp_order = client.futures_create_order(
            symbol=symbol,
            side='SELL' if side == 'BUY' else 'BUY',
            type='TAKE_PROFIT_MARKET',
            stopPrice=tp_price,
            closePosition='true'
        )
        # Stop Loss
        sl_order = client.futures_create_order(
            symbol=symbol,
            side='SELL' if side == 'BUY' else 'BUY',
            type='STOP_MARKET',
            stopPrice=sl_price,
            closePosition='true'
        )
        logging.info(f"OCO PLACED for {symbol}: TP {tp_price}, SL {sl_price}") [cite: 15]
        return tp_order, sl_order
    except Exception as e:
        logging.error(f"OCO ORDER ERROR: {e}") [cite: 41]
