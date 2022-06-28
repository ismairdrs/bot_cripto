from datetime import datetime
from database.repository import CriptoRepository
from auth.binance_auth import load_binance_creds


def store_ticker(list_ticker):
    repository = CriptoRepository()
    repository.insert(list_ticker)


def get_ticker():
    return client.get_ticker()


def handler(list_tickers):
    list_symbols = []
    for ticker in list_tickers:
        if "USDT" in ticker["symbol"]:
            ticker["time"] = now
            ticker["rise"] = 1 if float(ticker["priceChangePercent"]) > 0 else 0
            list_symbols.append(ticker)
    return list_symbols


client = load_binance_creds("/home/junior/botbtc/auth/auth.yml")
tickers = get_ticker()

now = datetime.timestamp(datetime.now())
tickers = handler(tickers)

store_ticker(tickers)
