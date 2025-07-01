import streamlit as st
from langchain_config import get_news_articles, summarize_articles, generate_summary

st.set_page_config(page_title="Equity Research News Tool", layout="wide")
st.title("📈 Equity Research News Tool")
st.markdown("Enter your query below to fetch & summarize the latest news articles.")

query = st.text_input("🔍 Your query", placeholder="e.g. Tesla Q2 earnings")

if st.button("Get News Summary"):
    if not query.strip():
        st.error("Please enter a non-empty query.")
    else:
        with st.spinner("Fetching top articles…"):
            articles = get_news_articles(query)

        if not articles:
            st.warning("No articles found for that query.")
        else:
            st.subheader("🔗 Top articles:")
            for art in articles:
                st.markdown(f"- [{art['title']}]({art['url']})")

            snippets = summarize_articles(articles)
            with st.spinner("Generating Grok summary…"):
                summary = generate_summary(query, snippets)

            st.subheader("📝 Grok-Generated Summary")
            st.markdown(summary)