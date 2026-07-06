import json

from Agents.strategy_agent import StrategyAgent


def main():

    with open("output/parsed_documents.json") as f:
        ingestion = json.load(f)

    with open("output/architecture_analysis.json") as f:
        architecture = json.load(f)

    with open("output/metrics_analysis.json") as f:
        metrics = json.load(f)

    agent = StrategyAgent()

    result = agent.run(
        ingestion,
        architecture,
        metrics
    )

    agent.save(result, "output/performance_strategy.json")

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()