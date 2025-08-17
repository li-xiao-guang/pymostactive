from abc import abstractmethod, ABC
from typing import Optional

import pandas as pd


class BaseDataProvider(ABC):

    @abstractmethod
    def get_stocks(self, count: int = 50) -> Optional[pd.DataFrame]:
        pass
