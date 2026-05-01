class ScoringAgent:
    """Creates a simple 0-100 research score from liquidity, volume, and risk signals."""

    @staticmethod
    def _to_float(value, default=0.0):
        try:
            return float(value or default)
        except (TypeError, ValueError):
            return default

    def score(self, data: dict, risks: list[str]) -> int:
        score = 70

        liquidity = self._to_float(data.get("liquidity_usd"))
        volume = self._to_float(data.get("volume_24h"))
        price_change = abs(self._to_float(data.get("price_change_24h")))

        if liquidity > 1_000_000:
            score += 10
        elif liquidity < 100_000:
            score -= 15

        if volume > 500_000:
            score += 10
        elif volume < 10_000:
            score -= 5

        if price_change > 50:
            score -= 10
        elif price_change > 30:
            score -= 5

        # Ignore the default "no obvious risk" message when applying penalty.
        real_risks = [r for r in risks if not r.startswith("暂未发现")]
        score -= len(real_risks) * 5

        return max(0, min(int(score), 100))
