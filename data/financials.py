class DailyFinancialsSnapshot:
    def __init__(self, subgraph, start_timestamp: int):
        self.subgraph = subgraph
        self.start_timestamp = start_timestamp
    
    def get_fields(self):
        financials = self.subgraph.Query.financialsDailySnapshots(
            where=[
                self.subgraph.FinancialsDailySnapshot.timestamp > self.start_timestamp
            ]
        )
        
        return [
            financials.id,
            financials.totalValueLockedUSD,
            financials.dailySupplySideRevenueUSD,
            financials.cumulativeSupplySideRevenueUSD,
            financials.dailyProtocolSideRevenueUSD,
            financials.cumulativeProtocolSideRevenueUSD,
            financials.dailyTotalRevenueUSD,
            financials.cumulativeTotalRevenueUSD,
            financials.timestamp,
        ]
    