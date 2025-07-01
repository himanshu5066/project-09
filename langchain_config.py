import os
from dotenv import load_dotenv

# ─── Load environment ────────────────────────────────────────────────────────────
load_dotenv()
GROK_API_KEY = os.getenv("GROK_API_KEY")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

if not GROK_API_KEY:
    raise ValueError("Please set GROK_API_KEY in your .env")
if not NEWSAPI_KEY:
    raise ValueError("Please set NEWSAPI_KEY in your .env")

# ─── LangChain & NewsAPI setup ──────────────────────────────────────────────────
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from newsapi import NewsApiClient

# Point the OpenAI-compatible client at xAI’s Grok endpoint
llm = OpenAI(
    model="grok-3-beta",
    openai_api_key=GROK_API_KEY,
    openai_api_base="https://api.x.ai"
)

prompt = PromptTemplate(
    template="""
You are an AI assistant helping an equity research analyst.
Given the following query and the provided news article summaries,
provide an overall summary.

Query: {query}
Summaries: {summaries}
""",
    input_variables=["query", "summaries"]
)

llm_chain = LLMChain(prompt=prompt, llm=llm)
newsapi = NewsApiClient(api_key=NEWSAPI_KEY)

def get_news_articles(query: str, max_results: int = 3) -> list[dict]:
    """Fetch top `max_results` articles for `query`."""
    resp = newsapi.get_everything(
        q=query,
        language="en",
        sort_by="relevancy",
        page_size=max_results,
    )
    return resp.get("articles", [])

def summarize_articles(articles: list[dict]) -> str:
    """Concatenate descriptions into one text blob."""
    snippets = [art.get("description", "") for art in articles]
    return "\n\n".join(snippets)

def generate_summary(query: str, snippets: str) -> str:
    """
    Attempt Grok summarization; on any error (rate limit, network, etc.),
    fall back to raw snippets and show the exception type.
    """
    try:
        return llm_chain.run({"query": query, "summaries": snippets})
    except Exception as e:
        return (
            f"**⚠️ Grok summarization failed ({e.__class__.__name__}); "
            "showing raw article descriptions below:**\n\n"
            + snippets
        )