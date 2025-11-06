from fastapi import FastAPI, Request
from backend.gpi_query import query_gpi
from backend.llm import parse_query

app = FastAPI()

@app.post("/query")
async def query_endpoint(request: Request):
    data = await request.json()
    user_input = data.get("query")
    sparql_query = parse_query(user_input)
    results = query_gpi(sparql_query)
    return {"results": results}
