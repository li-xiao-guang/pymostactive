from typing import Optional

import pandas as pd

from tradingview.tradingview_china_stock_provider import TradingViewChinaStockProvider
from tradingview.tradingview_crypto_provider import TradingViewCryptoProvider
from tradingview.tradingview_etf_provider import TradingViewETFProvider
from tradingview.tradingview_hk_stock_provider import TradingViewHKStockProvider
from tradingview.tradingview_japan_stock_provider import TradingViewJapanStockProvider
from tradingview.tradingview_stock_provider import TradingViewStockProvider
from tradingview.tradingview_uk_stock_provider import TradingViewUKStockProvider
from yahoo.yahoo_crypto_provider import YahooCryptoProvider
from yahoo.yahoo_etf_provider import YahooETFProvider
from yahoo.yahoo_stock_provider import YahooStockProvider


class MostActive:

    @staticmethod
    def download(resource: str = 'all',
                 market: str = 'us',
                 category: str = 'all',
                 count: int = 50) -> Optional[pd.DataFrame]:
        providers = []

        if resource == 'yahoo' or resource == 'all':
            if market == 'us' or market == 'all':
                if category == 'stock' or category == 'all':
                    providers.append(YahooStockProvider())
                if category == 'etf' or category == 'all':
                    providers.append(YahooETFProvider())
                if category == 'crypto' or category == 'all':
                    providers.append(YahooCryptoProvider())

        if resource == 'tradingview' or resource == 'all':
            if market == 'us' or market == 'all':
                if category == 'stock' or category == 'all':
                    providers.append(TradingViewStockProvider())
                if category == 'etf' or category == 'all':
                    providers.append(TradingViewETFProvider())
                if category == 'crypto' or category == 'all':
                    providers.append(TradingViewCryptoProvider())
            if market == 'uk' or market == 'all':
                if category == 'stock' or category == 'all':
                    providers.append(TradingViewUKStockProvider())
            if market == 'china' or market == 'all':
                if category == 'stock' or category == 'all':
                    providers.append(TradingViewChinaStockProvider())
            if market == 'hk' or market == 'all':
                if category == 'stock' or category == 'all':
                    providers.append(TradingViewHKStockProvider())
            if market == 'japan' or market == 'all':
                if category == 'stock' or category == 'all':
                    providers.append(TradingViewJapanStockProvider())

        combined_df = None
        for provider in providers:
            df = provider.get_stocks(count)
            if df is not None:
                if combined_df is None:
                    combined_df = df
                else:
                    combined_df = pd.concat([combined_df, df]).drop_duplicates(
                        subset='symbol', keep='first'
                    )

        if combined_df is not None:
            combined_df = combined_df.reset_index(drop=True)
        return combined_df


if __name__ == '__main__':
    most_active = MostActive()
    result = most_active.download(market='uk')
    if result is not None:
        print(result)
    else:
        print(f"download failed from tradingview")
