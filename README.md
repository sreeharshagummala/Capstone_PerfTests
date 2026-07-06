## Capstone Project

## Tech Stack
Python
LangChain
OpenAI

1. Get Project Docs
   ProjectSampleDocs - Has all project related documents like Architecture, Performance Testing Guidelines, Previous Performance Report, etc.
2. Parse Documents (Parse the documents and extract relevant information using LangChain)
   pip install pandas pyyaml python-dotenv pydantic
   Parsing folder - Contains different files which parse specific type of docs. 
   ingestion_pipeline.py - This is the main file which calls all other parsing files and creates a single YAML file with all the parsed information.