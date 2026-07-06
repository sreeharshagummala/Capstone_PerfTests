import json

from Agents.architecture_agent import ArchitectureAnalyzerAgent


def main():

    with open("output/parsed_documents.json") as f:
        ingestion = json.load(f)

    agent = ArchitectureAnalyzerAgent()

    result = agent.analyze(ingestion)

    agent.save(
        result,
        "output/architecture_analysis.json",
    )

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()