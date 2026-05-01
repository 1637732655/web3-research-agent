class RiskAgent:
    """Detects simple market and liquidity risks from token data."""

    @staticmethod
    def _to_float(value, default=0.0):
        try:
            return float(value or default)
        except (TypeError, ValueError):
            return default

    def analyze(self, data: dict):
        risks = []

        liquidity = self._to_float(data.get("liquidity_usd"))
        volume = self._to_float(data.get("volume_24h"))
        fdv = self._to_float(data.get("fdv"))
        market_cap = self._to_float(data.get("market_cap"))
        price_change = self._to_float(data.get("price_change_24h"))

        if liquidity < 100_000:
            risks.append("流动性较低，买卖滑点、砸盘和价格操控风险较高。")

        if fdv > 0 and liquidity > 0 and fdv / liquidity > 100:
            risks.append("FDV 与流动性比例过高，估值可能偏虚，需要关注解锁和抛压。")

        if market_cap > 0 and liquidity > 0 and market_cap / liquidity > 50:
            risks.append("市值与流动性比例偏高，真实可交易深度可能不足。")

        if abs(price_change) > 30:
            risks.append("24 小时价格波动过大，短期投机情绪较强。")

        if liquidity > 0 and volume > liquidity * 5:
            risks.append("成交量相对流动性异常偏高，可能存在刷量、短期炒作或高频套利行为。")

        if not risks:
            risks.append("暂未发现明显高风险信号，但仍需要结合项目背景、合约安全、团队信息和代币解锁进一步判断。")

        return risks
