import streamlit as st
import requests

st.title("Getty Provenance Chatbot")
user_input = st.text_input("Ask about provenance data:")

if st.button("Submit"):
    response = requests.post("http://localhost:8000/query", json={"query": user_input})
    st.json(response.json())
