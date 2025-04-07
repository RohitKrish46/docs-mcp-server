A lightweight MCP server that searches and retrieves relevant documentation content from popular AI libraries like LangChain, LlamaIndex, and OpenAI using a combination of web search and content parsing.

This project allows Language Models to query and fetch up-to-date documentation content dynamically, acting as a bridge between LLMs and external doc sources.


## 🚀 Features

Web Search Integration:
Utilizes Serper to search Google and retrieve the top documentation pages for a given query.

Content Extraction:
Parses and extracts clean, readable text from the HTML pages using BeautifulSoup.

LLM Tool Integration:
Exposes the get_docs tool that can be used within an LLM agent to query specific documentation sources.

## 🛠️Tool

get_docs(query: str, library: str)
This is the core tool provided by the MCP server.
It accepts:

query: The search term or phrase.

library: One of langchain, llama-index, or openai.

🔍 Searches for relevant documentation pages
📄 Fetches and parses clean text content
🧠 Sends the result back to the LLM for further reasoning and responses


📦 Setup

1. Clone the repository
```
git clone https://github.com/your-username/mcp-docs-search.git
cd mcp-docs-search
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Set your environment variables Create a .env file and add your Serper API key:
```
SERPER_API_KEY=your_serper_api_key
```

4. Run the MCP server
```
python main.py
```

## 📚 Supported Libraries
LangChain

LlamaIndex

OpenAI

More libraries can be easily added by updating the docs_urls dictionary.