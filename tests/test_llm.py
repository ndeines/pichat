from backend.llm import parse_query

def test_parse_query_format():
    query = "Show me paintings sold in Paris in the 18th century"
    sparql = parse_query(query)
    assert "SELECT" in sparql or "CONSTRUCT" in sparql
