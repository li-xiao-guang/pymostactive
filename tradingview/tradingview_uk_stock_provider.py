from typing import Optional

import pandas as pd

from base_data_provider import BaseDataProvider
from web_scraper import ScrapingConfig, WebScraper


class TradingViewUKStockProvider(BaseDataProvider):

    def get_stocks(self, count: int = 50) -> Optional[pd.DataFrame]:
        config_obj = ScrapingConfig(
            url='https://www.tradingview.com/markets/stocks-united-kingdom/market-movers-active/',
            symbol_tag='a',
            symbol_attrs={'class': 'tickerNameBox-GrtoTeat'},
            name_tag='sup',
            name_attrs={'class': 'tickerDescription-GrtoTeat'}
        )

        df = WebScraper.scrape_stocks(config_obj)
        if df is not None:
            df['market'] = 'uk'
            df['category'] = 'stock'

        return df.head(count) if df is not None else None
