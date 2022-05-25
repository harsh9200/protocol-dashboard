class DailyMetricsSnapshot:
    
    def __init__(self, subgraph, start_timestamp: int):
        self.subgraph = subgraph
        self.start_timestamp = start_timestamp
    
    def get_fields(self):
        metrics = self.subgraph.Query.usageMetricsDailySnapshots(
            where=[
                self.subgraph.UsageMetricsDailySnapshot.timestamp > self.start_timestamp
            ]
        )
        
        return [
            metrics.id,
            metrics.dailyActiveUsers,
            metrics.cumulativeUniqueUsers,
            metrics.dailyDepositCount,
            metrics.dailyWithdrawCount,
            metrics.dailyTransactionCount,
            metrics.timestamp,
        ]