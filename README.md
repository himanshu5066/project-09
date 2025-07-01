LLM Project: News Research Tool
This project is an AI-powered news summarization tool designed to assist equity research analysts in quickly accessing and summarizing relevant news articles using LangChain, OpenAI, NewsAPI, and Streamlit.

 Features
 Query-based news search via NewsAPI
 AI summarization of multiple articles using groq
 Streamlit web interface for seamless interaction
 Modular code using LangChain and PromptTemplates
 Easily configurable and extendable


 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/news-research-tool.git
cd news-research-tool
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or manually:

bash
Copy
Edit
pip install langchain openai streamlit newsapi-python python-dotenv
3. Add API Keys
Create a .env file and add:

ini
Copy
Edit
OPENAI_API_KEY=your-openai-api-key
NEWSAPI_KEY=your-newsapi-key
⚙️ Usage Instructions
Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
Interact via Web UI
Enter a financial query (e.g., "Tesla stock performance").

Click Get News to receive an AI-generated summary of relevant news.

 How It Works
User Input: A query is entered via the Streamlit interface.

News Retrieval: NewsAPI fetches the most relevant articles.

Summarization:
Descriptions are extracted from each article.
A LangChain LLMChain with a prompt template sends them to OpenAI for summarization.
Result Display: Final summary is rendered on the Streamlit app.

 Testing & Validation
 Confirmed basic functionality of query and summary flow.
 Validated quality and relevance of AI-generated summaries.

 Optional Enhancements
 User Authentication
 Improved UI/UX with advanced Streamlit components

 Save/Export Summaries
 Historical Analysis
 Dependencies
text
Copy
Edit
langchain
groq
streamlit
newsapi-python
python-dotenv
📚 Resources
groq API
NewsAPI Docs
LangChain Docs
Streamlit Docs

 License
This project is for educational purposes under MIT License.
Let me know if you'd like this exported as a .md file or if you want help pushing it to GitHub
