from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import httpx
import json
import os

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
def get_docs(query: str, library: str):
    """
    Search the docs for a given query and library,
    Supports langchain, llama-index, and openai.

    Args:
        query (str): The query to search for.
        library (str): The library to search in.

    Returns:
        List of dictionaries containing source URLs and extracted text
    """
    
def main():
    print("Hello from documentation!")


if __name__ == "__main__":
    main()
