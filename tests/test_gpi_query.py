from backend.gpi_query import query_gpi

def test_query_gpi():
    sample_query = "SELECT ?s WHERE { ?s ?p ?o } LIMIT 1"
    result = query_gpi(sample_query)
    assert "results" in result
