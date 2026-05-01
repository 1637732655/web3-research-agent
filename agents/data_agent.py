from services.dexscreener import DexScreenerService


class DataAgent:
    """Collects and normalizes token data from public Web3 data sources."""

    def __init__(self):
        self.dex_service = DexScreenerService()

    def collect_data(self, query: str):
        token_data = self.dex_service.search_token(query)
        if not token_data:
            return None

        base_token = token_data.get("baseToken") or {}
        liquidity = token_data.get("liquidity") or {}
        volume = token_data.get("volume") or {}
        price_change = token_data.get("priceChange") or {}

        return {
            "project_name": base_token.get("name"),
            "symbol": base_token.get("symbol"),
            "token_address": base_token.get("address"),
            "chain": token_data.get("chainId"),
            "dex": token_data.get("dexId"),
            "pair_address": token_data.get("pairAddress"),
            "price_usd": token_data.get("priceUsd"),
            "liquidity_usd": liquidity.get("usd", 0),
            "volume_24h": volume.get("h24", 0),
            "volume_6h": volume.get("h6", 0),
            "volume_1h": volume.get("h1", 0),
            "price_change_24h": price_change.get("h24", 0),
            "price_change_6h": price_change.get("h6", 0),
            "price_change_1h": price_change.get("h1", 0),
            "fdv": token_data.get("fdv", 0),
            "market_cap": token_data.get("marketCap", 0),
            "pair_url": token_data.get("url"),
        }
