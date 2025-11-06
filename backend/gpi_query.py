import requests


def query_gpi(sparql_query: str):
    endpoint = "https://data.getty.edu/provenance/sparql"
    headers = {"Accept": "application/sparql-results+json"}
    try:
        response = requests.get(endpoint, params={"query": sparql_query}, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        # Keep error messages concise for the API response
        raise RuntimeError(f"Query error: {e}")
