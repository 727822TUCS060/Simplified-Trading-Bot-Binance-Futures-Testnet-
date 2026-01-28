# Simplified-Trading-Bot-Binance-Futures-Testnet-
i have created simplified trading bot with the log files
To fulfill the **Report & Docs** requirement (10% of your grade), your `README.md` must be clear, professional, and explain exactly how to reproduce your results.

Create a file named `README.md` in your project root and paste the following content:

---

# Binance Futures Trading Bot

A CLI-based trading bot for **Binance USDT-M Futures** that supports core order types and advanced execution strategies with robust logging and validation.

## 📂 Project Structure

```text
[project_root]/
├── src/
│   ├── market_orders.py    # Logic for Market orders
│   ├── limit_orders.py     # Logic for Limit orders
│   └── advanced/           # Advanced execution strategies
│       ├── oco.py          # One-Cancels-the-Other logic
│       └── twap.py         # Time-Weighted Average Price strategy
├── bot.log                 # Structured execution logs
├── report.pdf              # Performance analysis & screenshots
├── README.md               # Setup and usage guide
└── requirements.txt        # Project dependencies

```

## 🛠 Setup Instructions

### 1. Prerequisites

* Python 3.8+ installed.
* A **Binance Futures Testnet** account.

### 2. Installation

Clone the repository and install the official Binance connector:

```bash
pip install python-binance

```

### 3. API Configuration

To run this bot, you must use **Binance Futures Testnet API Keys**.

1. Log in to the [Binance Futures Testnet](https://testnet.binancefuture.com/).
2. Generate an **API Key** and **Secret Key** from the dashboard.
3. Ensure **"Enable Futures"** is checked in your API restrictions.
4. Update the `api_key` and `api_secret` variables in the scripts within the `/src` folder.

## 🚀 Usage Guide

Run the scripts from the **project root** using the following command formats:

### Market Orders

```bash
python src/market_orders.py <SYMBOL> <SIDE> <QUANTITY>
# Example:
python src/market_orders.py BTCUSDT BUY 0.01

```

### Limit Orders

```bash
python src/limit_orders.py <SYMBOL> <SIDE> <QUANTITY> <PRICE>
# Example:
python src/limit_orders.py BTCUSDT BUY 0.01 45000

```

### TWAP Strategy (Advanced)

Splits a large order into smaller chunks over a set duration.

```bash
python src/advanced/twap.py <SYMBOL> <SIDE> <TOTAL_QTY> <DURATION_MINS>
# Example (Buy 0.03 BTC over 1 minute):
python src/advanced/twap.py BTCUSDT BUY 0.03 1

```

## 📝 Logging & Validation

* **Validation**: The bot validates symbols, quantities, and price thresholds before execution to prevent API errors.
* **Structured Logs**: All actions, including successful placements and error traces, are recorded in `bot.log` with high-precision timestamps.

<img width="1476" height="183" alt="image" src="https://github.com/user-attachments/assets/dcb8c1b9-91cc-491f-b802-81076d47d516" />

