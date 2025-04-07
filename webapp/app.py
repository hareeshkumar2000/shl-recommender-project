import streamlit as st
import requests

st.title("🔍 SHL Assessment Recommender")

query = st.text_area("Enter Job Description or Role", height=200)

if st.button("Recommend Assessments"):
    with st.spinner("Fetching recommendations..."):
        res = requests.get("http://localhost:8000/api/recommend", params={"query": query})
        data = res.json()
        for i, item in enumerate(data["results"], 1):
            st.markdown(f"### {i}. [{item['name']}]({item['url']})")
            st.write(f"**Remote Testing:** {item['remote_support']}")
            st.write(f"**Adaptive Support:** {item['adaptive_support']}")
            st.write(f"**Duration:** {item['duration']}")
            st.write(f"**Test Type:** {item['test_type']}")