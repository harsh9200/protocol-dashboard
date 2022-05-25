class Vault:
    def __init__(self, subgraph):
        self.subgraph = subgraph
    
    def get_fields(self):
        vault = self.subgraph.Query.vaults(
            first= 10,
            orderBy=self.subgraph.Vault.totalValueLockedUSD,
            orderDirection='desc',
        )
        
        return [
            vault.name,
            vault.totalValueLockedUSD,
            vault.inputTokenBalance,
            vault.outputTokenSupply,
        ]