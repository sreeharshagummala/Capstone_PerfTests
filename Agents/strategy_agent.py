import json
import os

from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

from Prompts.strategy_prompt import STRATEGY_PROMPT


class StrategyAgent:

    def __init__(self, model="gpt-4.1-mini", temperature=0):
        self.llm = ChatOpenAI(model=model, temperature=temperature)
        self.parser = JsonOutputParser()

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", STRATEGY_PROMPT),
            ("human", """
Architecture Analysis:
{architecture}

Metrics Analysis:
{metrics}

NFR:
{nfr}

API List:
{api}

Workload:
{workload}
""")
        ])

        self.chain = self.prompt | self.llm | self.parser

    def run(self, ingestion, architecture, metrics):

        result = self.chain.invoke({
            "architecture": json.dumps(architecture, indent=2),
            "metrics": json.dumps(metrics, indent=2),
            "nfr": ingestion["nfr_raw"],
            "api": json.dumps(ingestion["api"], indent=2),
            "workload": json.dumps(ingestion["workload"], indent=2)
        })

        return result

    def save(self, output, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(output, f, indent=4)