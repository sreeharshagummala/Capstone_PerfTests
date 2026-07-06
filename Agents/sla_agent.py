import json
import os

from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

from Prompts.sla_prompt import SLA_PROMPT


class SLAAgent:

    def __init__(self, model="gpt-4.1-mini", temperature=0):
        self.llm = ChatOpenAI(model=model, temperature=temperature)
        self.parser = JsonOutputParser()

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", SLA_PROMPT),
            ("human", """
NFR Benchmarks:
{nfr}

Metrics Analysis:
{metrics}

Architecture Analysis:
{architecture}
""")
        ])

        self.chain = self.prompt | self.llm | self.parser

    def run(self, ingestion, metrics, architecture):

        return self.chain.invoke({
            "nfr": ingestion["nfr_raw"],
            "metrics": json.dumps(metrics, indent=2),
            "architecture": json.dumps(architecture, indent=2),
        })

    def save(self, result, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(result, f, indent=4)