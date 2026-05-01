import requests


class DexScreenerService:
    """Service for fetching token / pair data from DexScreener public API."""

    BASE_URL = "https://api.dexscreener.com/latest/dex/search"

    def search_token(self, query: str):
        """Search token by symbol, project name, or contract address."""
        response = requests.get(self.BASE_URL, params={"q": query}, timeout=15)
        response.raise_for_status()
        data = response.json()
        pairs = data.get("pairs") or []
        if not pairs:
            return None

        # Prefer the pair with the highest liquidity, because search results may contain many small pools.
        pairs = sorted(
            pairs,
            key=lambda p: float((p.get("liquidity") or {}).get("usd") or 0),
            reverse=True,
        )
        return pairs[0]
