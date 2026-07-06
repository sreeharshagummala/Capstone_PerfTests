import json

from Agents.metrics_agent import MetricsAnalyzerAgent


def main():

    with open("output/parsed_documents.json") as f:
        ingestion = json.load(f)

    with open("output/architecture_analysis.json") as f:
        architecture = json.load(f)

    agent = MetricsAnalyzerAgent()

    result = agent.analyze(
        architecture,
        ingestion,
    )

    agent.save(
        result,
        "output/metrics_analysis.json",
    )

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()