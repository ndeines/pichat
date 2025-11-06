import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_query(user_input: str) -> str:
    prompt = f"Convert the following natural language query into a SPARQL query for the Getty Provenance Index:\n\n{user_input}\n\nSPARQL query:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that converts natural language into SPARQL queries."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response["choices"][0]["message"]["content"].strip()
