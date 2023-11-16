import ccxt
import json


def get_data(currency_pair, interval, market):
    if market == "Binance":
        market_name = ccxt.binance()
        data = market_name.fetch_ohlcv(currency_pair, interval)
        return data
    elif market == "Kucoin":
        market_name = ccxt.kucoin()
        data = market_name.fetch_ohlcv(currency_pair, interval)
        return data
    elif market == "Coinbase":
        market_name = ccxt.coinbase()
        data = market_name.fetch_ohlcv(currency_pair, interval)
        return data
    elif market == "YoBit":
        market_name = ccxt.yobit()
        data = market_name.fetch_ohlcv(currency_pair, interval)
        return data
    elif market == "Bybit":
        market_name = ccxt.bybit()
        data = market_name.fetch_ohlcv(currency_pair, interval)
        return data


def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


market = "Binance"
currency_pair = 'BTC/USDT'
interval = '1d'

data = get_data(currency_pair, interval, market)
save_to_json(data, 'data.json')
print(str(data[0][1]))
