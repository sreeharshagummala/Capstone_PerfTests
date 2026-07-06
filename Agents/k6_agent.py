import json
import os

from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from Prompts.k6_prompt import K6_PROMPT


class K6Agent:

    def __init__(self, model="gpt-4.1-mini", temperature=0):
        self.llm = ChatOpenAI(model=model, temperature=temperature)
        self.parser = StrOutputParser()

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", K6_PROMPT),
            ("human", """
Performance Strategy:
{strategy}

SLA Targets:
{sla}

API List:
{api}

Workload:
{workload}
""")
        ])

        self.chain = self.prompt | self.llm | self.parser

    def run(self, strategy, sla, ingestion):

        return self.chain.invoke({
            "strategy": json.dumps(strategy, indent=2),
            "sla": json.dumps(sla, indent=2),
            "api": json.dumps(ingestion["api"], indent=2),
            "workload": json.dumps(ingestion["workload"], indent=2),
        })

    def save(self, code, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(code)