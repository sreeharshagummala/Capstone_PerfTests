## Capstone Project

## Tech Stack
Python
LangChain
OpenAI

## Dependencies
pip install langchain
pip install langchain-openai
pip install langchain-community #This has classes that allow us to access open source models
pip install langgraph
pip install python-dotenv #This is for loading environment variables from .env file. We can also set environment variables directly in the system without using this package.
pip install streamlit
pip install pandas pyyaml python-dotenv pydantic

## Notes
1. Get Project Docs
   ProjectSampleDocs - Has all project related documents like Architecture, Performance Testing Guidelines, Previous Performance Report, etc.
2. Parse Documents (Parse the documents and extract relevant information using LangChain)
   Parsing folder - Contains different files which parse specific type of docs. 
   ingestion_pipeline.py - This is the main file which calls all other parsing files and creates a single YAML file with all the parsed information.