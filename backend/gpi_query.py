import requests

def query_gpi(sparql_query: str):
    endpoint = "https://data.getty.edu/provenance/sparql"
    headers = {"Accept": "application/sparql-results+json"}
    response = requests.get(endpoint, params={"query": sparql_query}, headers=headers)
    return response.json()
