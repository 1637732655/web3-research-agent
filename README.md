# Web3 Research Agent

一个基于 Python 的 Web3 项目研究 Agent。用户输入项目名称、代币名称或合约地址后，系统会自动查询 DexScreener 数据，完成项目基础信息整理、赛道判断、风险识别、评分和研究报告生成。

## 项目解决的问题

Web3 项目信息分散在 RootData、DeFiLlama、DexScreener、CoinMarketCap 等平台。新人手动判断项目时，容易只看价格涨跌，忽略 TVL、Volume、Liquidity、FDV、代币流动性和赛道逻辑。

本项目通过 Agent 流程把研究步骤结构化，帮助用户更快完成项目初筛。

## 核心流程

1. Data Agent：收集 DexScreener 上的代币和交易对数据。
2. Category Agent：根据项目名称、符号和交易信息判断项目赛道。
3. Risk Agent：识别低流动性、高 FDV、价格剧烈波动、成交量异常等风险。
4. Scoring Agent：根据指标生成 0-100 的初步评分。
5. Report Agent：输出结构化 Markdown 研究报告。

## 项目结构

```text
web3-research-agent/
├── main.py
├── agents/
│   ├── data_agent.py
│   ├── category_agent.py
│   ├── risk_agent.py
│   ├── report_agent.py
│   └── web3_research_agent.py
├── services/
│   └── dexscreener.py
├── utils/
│   └── scoring.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 安装

```bash
git clone https://github.com/your-name/web3-research-agent.git
cd web3-research-agent
pip install -r requirements.txt
```

## 运行

```bash
python main.py
```

## 示例输入

```text
ASTER
```

也可以输入代币合约地址。

## 示例输出

系统会输出：

- 项目名称
- 代币符号
- 所属链
- 当前价格
- 24 小时成交量
- 流动性
- FDV
- 赛道判断
- 风险分析
- 综合评分
- Agent 结论

## 后续计划

- 接入 DeFiLlama TVL 数据
- 接入 CoinMarketCap 市值和交易所价格数据
- 增加 RootData 项目背景和融资信息
- 增加多项目横向对比表
- 增加定时监控和 Telegram Bot 提醒
- 增加 Web 前端 Demo

## 风险提示

本项目只用于学习和研究，不构成投资建议。Web3 项目风险较高，任何判断都需要结合合约安全、团队背景、代币解锁、市场环境和个人风险承受能力。
# web3-research-agent
