from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def parse_query(user_input: str) -> str:
    """Convert natural language into a SPARQL query using the OpenAI API.

    Raises RuntimeError on LLM failure or ValueError for empty input.
    """
    if not user_input:
        raise ValueError("Empty user input")

    prompt = f"Convert the following natural language query into a SPARQL query for the Getty Provenance Index:\n\n{user_input}\n\nSPARQL query:"
    try:
        response = await client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that converts natural language into SPARQL queries."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        # Defensive access of the content
        content = response["choices"][0]["message"]["content"].strip()
        return content
    except Exception as e:
        # Surface a clear error for the FastAPI layer to handle
        raise RuntimeError(f"LLM error: {e}")
