class CategoryAgent:
    """Classifies a Web3 project into a broad sector based on available text signals."""

    def classify(self, data: dict) -> str:
        name = (data.get("project_name") or "").lower()
        symbol = (data.get("symbol") or "").lower()
        dex = (data.get("dex") or "").lower()
        text = f"{name} {symbol} {dex}"

        if any(k in text for k in ["perp", "future", "derivative", "options"]):
            return "Derivatives"
        if any(k in text for k in ["lend", "borrow", "credit", "loan"]):
            return "Lending"
        if any(k in text for k in ["stake", "staking", "lst", "liquid staking"]):
            return "Liquid Staking"
        if any(k in text for k in ["yield", "farm", "vault", "earn"]):
            return "Yield"
        if dex:
            return "DEX / Trading"

        return "Unknown / Need More Research"
