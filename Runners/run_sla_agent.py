import json

from Agents.sla_agent import SLAAgent


def main():

    with open("output/parsed_documents.json") as f:
        ingestion = json.load(f)

    with open("output/metrics_analysis.json") as f:
        metrics = json.load(f)

    with open("output/architecture_analysis.json") as f:
        architecture = json.load(f)

    agent = SLAAgent()

    result = agent.run(
        ingestion,
        metrics,
        architecture
    )

    agent.save(result, "output/sla_analysis.json")

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()