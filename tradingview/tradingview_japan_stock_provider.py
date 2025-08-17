from typing import Optional

import pandas as pd

from base_data_provider import BaseDataProvider
from web_scraper import ScrapingConfig, WebScraper


class TradingViewJapanStockProvider(BaseDataProvider):

    def get_stocks(self, count: int = 50) -> Optional[pd.DataFrame]:
        config_obj = ScrapingConfig(
            url='https://www.tradingview.com/markets/stocks-japan/market-movers-active/',
            symbol_tag='a',
            symbol_attrs={'class': 'tickerNameBox-GrtoTeat'},
            name_tag='sup',
            name_attrs={'class': 'tickerDescription-GrtoTeat'}
        )

        df = WebScraper.scrape_stocks(config_obj)
        if df is not None:
            df['symbol'] = df['symbol'].apply(self._add_exchange_suffix)
            df['market'] = 'japan'
            df['category'] = 'stock'

        return df.head(count) if df is not None else None

    @staticmethod
    def _add_exchange_suffix(symbol: str) -> str:
        return f"{symbol}.T"
