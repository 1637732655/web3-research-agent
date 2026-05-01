from datetime import datetime


class ReportAgent:
    """Generates a readable Markdown research report."""

    @staticmethod
    def _fmt_money(value):
        try:
            value = float(value or 0)
            return f"${value:,.2f}"
        except (TypeError, ValueError):
            return str(value)

    def generate(self, data: dict, category: str, risks: list[str], score: int) -> str:
        risk_text = "\n".join([f"- {risk}" for risk in risks])

        return f"""
# Web3 Research Agent 项目分析报告

生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## 一、项目基础信息

- 项目名称：{data.get("project_name")}
- 代币符号：{data.get("symbol")}
- 合约地址：{data.get("token_address")}
- 所属链：{data.get("chain")}
- 交易平台：{data.get("dex")}
- 交易对地址：{data.get("pair_address")}
- 当前价格：{data.get("price_usd")} USD
- 24小时成交量：{self._fmt_money(data.get("volume_24h"))}
- 流动性：{self._fmt_money(data.get("liquidity_usd"))}
- FDV：{self._fmt_money(data.get("fdv"))}
- 市值：{self._fmt_money(data.get("market_cap"))}
- 24小时涨跌幅：{data.get("price_change_24h")}%

## 二、Agent 赛道判断

该项目初步判断为：**{category}**

## 三、风险分析

{risk_text}

## 四、综合评分

项目初步评分：**{score}/100**

## 五、Agent 结论

该项目可以作为初步研究对象，但不建议只根据价格涨跌做判断。  
需要继续结合项目官网、团队背景、融资情况、TVL、合约安全、代币解锁和社区活跃度进行综合分析。

数据来源：{data.get("pair_url")}
""".strip()
