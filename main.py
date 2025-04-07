from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import httpx
import json
import os
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
load_dotenv()

mcp = FastMCP("docs")

USER_AGENT = "docs-app/1.0"

SERPER_URL = "https://google.serper.dev/search"

docs_urls = {
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable",
    "openai": "platform.openai.com/docs"
}

# find relavant documentation pages for our library
async def search_web(query:str) -> dict | None:
    # getting top 2 results from the search
    payload = json.dumps({"q":query, "num":2})

    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        try: 
            response = await client.post(
                SERPER_URL, headers=headers, data=payload, timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException:
            return {"organic": []}

# fetch the content of a URL
async def fetch_url(url: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            return text
        except httpx.TimeoutException:
            return "Timeout error"

@mcp.tool()
async def get_docs(query: str, library: str):
    """
    Search the docs for a given query and library,
    Supports langchain, llama-index, and openai.

    Args:
        query (str): The query to search for.
        library (str): The library to search in.

    Returns:
        Text from the documentation.
    """
    if library not in docs_urls:
        raise ValueError(f"Library {library} not supported by this tool")
    query = f"site:{docs_urls[library]} {query}"
    results = await search_web(query)
    if len(results["organic"]) == 0:
        return "No results found"
    
    test_text = """
Chroma
    This notebook covers how to get started with the Chroma vector store.

    Chroma is a AI-native open-source vector database focused on developer productivity and happiness. Chroma is licensed under Apache 2.0. View the full docs of Chroma at this page, and find the API reference for the LangChain integration at this page.

    Setup
    To access Chroma vector stores you'll need to install the langchain-chroma integration package.

    pip install -qU "langchain-chroma>=0.1.2"

    Credentials
    You can use the Chroma vector store without any credentials, simply installing the package above is enough!

    If you want to get best in-class automated tracing of your model calls you can also set your LangSmith API key by uncommenting below:

    # os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
    # os.environ["LANGSMITH_TRACING"] = "true"
"""
    text = ""
    for result in results["organic"]:
        text += await fetch_url(result["link"])
    return test_text

def main():
    print("Hello from documentation!")


if __name__ == "__main__":
    mcp.run(transport="stdio")
