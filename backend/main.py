from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import asyncio
from backend.gpi_query import query_gpi
from backend.llm import parse_query

app = FastAPI()


@app.post("/query")
async def query_endpoint(request: Request):
    data = await request.json()
    user_input = data.get("query")
    if not user_input:
        return JSONResponse({"error": "Missing 'query' in body."}, status_code=400)

    loop = asyncio.get_event_loop()
    try:
        # Run blocking network/IO in the default executor so we don't block the event loop
        sparql_query = await loop.run_in_executor(None, parse_query, user_input)
        results = await loop.run_in_executor(None, query_gpi, sparql_query)
        return {"results": results}
    except Exception as e:
        # Return a JSON error rather than raising a 500 without context
        return JSONResponse({"error": str(e)}, status_code=500)
