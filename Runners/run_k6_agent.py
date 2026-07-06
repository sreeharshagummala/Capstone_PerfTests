import json

from Agents.k6_agent import K6Agent


def main():

    with open("output/performance_strategy.json") as f:
        strategy = json.load(f)

    with open("output/sla_analysis.json") as f:
        sla = json.load(f)

    with open("output/parsed_documents.json") as f:
        ingestion = json.load(f)

    agent = K6Agent()

    script = agent.run(
        strategy,
        sla,
        ingestion
    )

    agent.save(script, "output/load_test.js")

    print("k6 script generated successfully → output/load_test.js")


if __name__ == "__main__":
    main()