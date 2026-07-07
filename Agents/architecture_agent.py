import json
import os
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from Prompts.architecture_prompt import ARCHITECTURE_ANALYZER_PROMPT
from Agents.base_agent import BaseAgent


class ArchitectureAnalyzerAgent(BaseAgent):

    def __init__(
            self,
            model="gpt-4.1-mini",
            temperature=0,
    ):
        super().__init__(model=model, temperature=temperature)

        self.parser = JsonOutputParser()

        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", ARCHITECTURE_ANALYZER_PROMPT),
                (
                    "human",
                    """
                        Architecture Document:
                        {architecture}
                        
                        OpenAPI:
                        {api}
                        
                        Deployment:
                        {deployment}
                        
                        Non Functional Requirements:
                        {nfr}
                            """),
            ]
        )

        self.chain = self.prompt | self.llm | self.parser

    def analyze(self, ingestion_json):

        result = self.chain.invoke(
            {
                "architecture": ingestion_json["architecture_raw"],
                "api": json.dumps(ingestion_json["api"], indent=2),
                "deployment": json.dumps(
                    ingestion_json["deployment"],
                    indent=2,
                ),
                "nfr": ingestion_json["nfr_raw"],
            }
        )

        return result

    def save(self, result, output_path):

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w") as f:
            json.dump(result, f, indent=4)