from agents.web3_research_agent import Web3ResearchAgent


if __name__ == "__main__":
    query = input("请输入项目名称、代币名称或合约地址：").strip()
    if not query:
        print("请输入有效内容。")
    else:
        agent = Web3ResearchAgent()
        result = agent.run(query)
        print(result)
