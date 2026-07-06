import json
import os

from dotenv import load_dotenv

load_dotenv()

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from Prompts.metrics_prompt import METRICS_ANALYZER_PROMPT


class MetricsAnalyzerAgent:

    def __init__(
            self,
            model="gpt-4.1-mini",
            temperature=0,
    ):

        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature,
        )

        self.parser = JsonOutputParser()

        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", METRICS_ANALYZER_PROMPT),
                (
                    "human",
                    """
Architecture Analysis

{architecture}

Historical Metrics

{metrics}

Infrastructure Metrics

{infrastructure}

Previous Report

{previous_report}
                    """,
                ),
            ]
        )

        self.chain = self.prompt | self.llm | self.parser

    def analyze(
            self,
            architecture_analysis,
            ingestion_json,
    ):

        return self.chain.invoke(
            {
                "architecture": json.dumps(
                    architecture_analysis,
                    indent=2,
                ),
                "metrics": json.dumps(
                    ingestion_json["metrics"],
                    indent=2,
                ),
                "infrastructure": json.dumps(
                    ingestion_json["infrastructure"],
                    indent=2,
                ),
                "previous_report": ingestion_json[
                    "previous_report_raw"
                ],
            }
        )

    def save(self, result, output_path):

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w") as f:
            json.dump(result, f, indent=4)