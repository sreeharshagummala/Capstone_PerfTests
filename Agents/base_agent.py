import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
DEFAULT_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class BaseAgent:
    """Small helper base class to centralize LLM initialization.

    Usage:
        class MyAgent(BaseAgent):
            def __init__(self, model="gpt-4.1-mini", temperature=0):
                super().__init__(model=model, temperature=temperature)
                # self.llm is available
    """

    def __init__(self, model: str = "gpt-4.1-mini", temperature: float = 0, api_key: str | None = None):
        if api_key is None:
            api_key = DEFAULT_OPENAI_API_KEY

        self.llm = ChatOpenAI(
            model=model,
            api_key=api_key,
            temperature=temperature,
        )

