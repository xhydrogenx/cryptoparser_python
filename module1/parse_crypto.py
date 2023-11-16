import ccxt
import json


def get_data(currency_pair, interval, market):
    markets = {
        "binance": ccxt.binance(),
        "kucoin": ccxt.kucoin(),
        "coinbase": ccxt.coinbase(),
        "yoBit": ccxt.yobit(),
        "bybit": ccxt.bybit()
    }

    if market in markets:
        market_name = markets[market]
        data = market_name.fetch_ohlcv(currency_pair, interval)
        return data
    else:
        raise ValueError(f"Unknown market: {market}")


def save_to_json(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)
