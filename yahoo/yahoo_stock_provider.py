from typing import Optional

import pandas as pd

from base_data_provider import BaseDataProvider
from web_scraper import ScrapingConfig, WebScraper


class YahooStockProvider(BaseDataProvider):
    def get_stocks(self, count: int = 50) -> Optional[pd.DataFrame]:

        config_obj = ScrapingConfig(
            url='https://finance.yahoo.com/markets/stocks/most-active/?start=0&count=100',
            parent_tag='table',
            symbol_tag='span',
            symbol_attrs={'class': 'symbol'},
            name_tag='a',
            name_attrs={'class': 'ticker'}
        )

        df = WebScraper.scrape_stocks(config_obj)
        if df is not None:
            df['market'] = 'us'
            df['category'] = 'stock'

        return df.head(count) if df is not None else None
