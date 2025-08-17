from typing import Optional

import pandas as pd

from tradingview.tradingview_china_stock_provider import TradingViewChinaStockProvider
from tradingview.tradingview_etf_provider import TradingViewETFProvider
from tradingview.tradingview_stock_provider import TradingViewStockProvider
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

        if resource == 'tradingview' or resource == 'all':
            if market == 'us' or market == 'all':
                if category == 'stock' or category == 'all':
                    providers.append(TradingViewStockProvider())
                if category == 'etf' or category == 'all':
                    providers.append(TradingViewETFProvider())
            if market == 'china' or market == 'all':
                if category == 'stock' or category == 'all':
                    providers.append(TradingViewChinaStockProvider())

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
    result = most_active.download(market='us')
    if result is not None:
        print(result)
    else:
        print(f"download failed from tradingview")
