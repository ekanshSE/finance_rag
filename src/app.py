import streamlit as st
from rag_pipeline import retrieve_and_generate

st.title("Financial Analysis RAG Demo")
query = st.text_input("Enter your query:")
if st.button("Submit"):
    result = retrieve_and_generate(query)
    st.write(result)
