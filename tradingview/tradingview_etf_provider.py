from typing import Optional

import pandas as pd

from base_data_provider import BaseDataProvider
from web_scraper import ScrapingConfig, WebScraper


class TradingViewETFProvider(BaseDataProvider):

    def get_stocks(self, count: int = 50) -> Optional[pd.DataFrame]:
        config_obj = ScrapingConfig(
            url='https://www.tradingview.com/markets/etfs/funds-most-traded/',
            symbol_tag='a',
            symbol_attrs={'class': 'tickerNameBox-GrtoTeat'},
            name_tag='sup',
            name_attrs={'class': 'tickerDescription-GrtoTeat'}
        )

        df = WebScraper.scrape_stocks(config_obj)
        if df is not None:
            df['market'] = 'us'
            df['category'] = 'etf'

        return df.head(count) if df is not None else None
