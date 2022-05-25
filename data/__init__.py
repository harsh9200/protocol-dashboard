import pytz
import datetime
from subgrounds.subgrounds import Subgrounds

from data.vault import Vault
from data.metrics import DailyMetricsSnapshot
from data.financials import DailyFinancialsSnapshot

RANGE = {
    "24H": 1,
    "7D": 7,
    "1M": 30,
    "3M": 90
}


class SubgraphData:
    def __init__(self, url: str, number_of_days: int):
        self.url = url
        self.start_timestamp = (
            datetime.datetime.now() - datetime.timedelta(number_of_days)
        ).timestamp()

        self.subgrounds = Subgrounds()
        self.subgraph = self.subgrounds.load_subgraph(url)

        self.dataframe = self.query()

    def query(self):
        Metrics = DailyMetricsSnapshot(self.subgraph, int(self.start_timestamp))
        Financials = DailyFinancialsSnapshot(self.subgraph, int(self.start_timestamp))
        vault = Vault(self.subgraph)

        return self.subgrounds.query_df(Metrics.get_fields() + Financials.get_fields() + vault.get_fields())
