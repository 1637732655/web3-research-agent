from agents.data_agent import DataAgent
from agents.category_agent import CategoryAgent
from agents.risk_agent import RiskAgent
from agents.report_agent import ReportAgent
from utils.scoring import ScoringAgent


class Web3ResearchAgent:
    """Main coordinator for the Web3 multi-agent research workflow."""

    def __init__(self):
        self.data_agent = DataAgent()
        self.category_agent = CategoryAgent()
        self.risk_agent = RiskAgent()
        self.scoring_agent = ScoringAgent()
        self.report_agent = ReportAgent()

    def run(self, query: str) -> str:
        data = self.data_agent.collect_data(query)

        if not data:
            return "未找到相关项目或代币数据，请检查输入内容。"

        category = self.category_agent.classify(data)
        risks = self.risk_agent.analyze(data)
        score = self.scoring_agent.score(data, risks)

        return self.report_agent.generate(data, category, risks, score)
