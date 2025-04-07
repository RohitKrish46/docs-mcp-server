# 📚 MCP Docs Search Server

A lightweight MCP server that searches and retrieves relevant documentation content from popular AI libraries like LangChain, LlamaIndex, and OpenAI using a combination of web search and content parsing.

This project allows Language Models to query and fetch up-to-date documentation content dynamically, acting as a bridge between LLMs and external doc sources.

## Model Context Protocol (MCP)
The Model Context Protocol is an open standard that enables developers to build secure, two-way connections between their data sources and AI-powered tools. The architecture is straightforward: developers can either expose their data through MCP servers or build AI applications (MCP clients) that connect to these servers.

 ### LLMs in Isolation

> LLMs alone are limited — their true potential is unlocked when integrated with tools and services via frameworks like MCP.


![LLM_on_its_own](https://github.com/user-attachments/assets/a27664b7-ab6f-41e8-ad2e-08d710fa12f7)

1.  LLMs without tools, LLMs are static and have limited utility.

2. With tools, they become interactive, but orchestration can be messy.

3. With MCP, LLMs gain a scalable, plug-and-play interface to real-world services, making them much more practical and powerful in production environments.


### MCP Ecosystem


The MCP Server acts as the translator/interface between LLMs and services.

> MCP (Modular Capability Provider) standardizes how LLMs interact with external tools/services — promoting interoperability, modularity, and cleaner interfaces.


![MCP_ecosystem](https://github.com/user-attachments/assets/f493ccd3-6746-49a3-9b1a-7ef13d8fa45b)



This structure decentralizes responsibility:

1. Tool providers build and maintain their own MCP Server implementation.

2. LLMs just need to speak the MCP protocol.

![MCP](https://github.com/user-attachments/assets/1046aca4-c86d-4664-ac03-868bd4b9a5bf)


**Purpose and Vision:**

- Standardize communication between LLMs and external tools

- Avoid bespoke integrations

- Encourage a scalable ecosystem of services (like a plugin architecture)


## 🚀 Features

🔍 Web Search Integration
Uses the Serper API to query Google and retrieve the top documentation pages related to a given search query.

🧹 Clean Content Extraction
Parses HTML content using BeautifulSoup to extract clean, human-readable text—stripping away unnecessary tags, ads, or navigation content.

🤖 Seamless LLM Tooling
Exposes a structured get_docs tool that can be used within LLM agents (e.g., Claude, GPT) to query specific libraries in real time.


## 🛠️Tool

`get_docs(query: str, library: str)`

This is the core tool provided by the MCP server.
It accepts:

query: The search term or phrase.

library: One of langchain, llama-index, or openai.

### Workflow
1. 🔍 Searches for relevant documentation pages
2. 📄 Fetches and parses clean text content
3. 🧠 Sends the result back to the LLM for further reasoning and responses


## 📦 Setup

1. Clone the repository
```
git clone https://github.com/your-username/mcp-docs-search.git
cd mcp-docs-search
```
2. Create a virtual Envoirment using uv and activate it

```
uv venv .venv

.\.venv\Scripts\activate
```


3. Install dependencies
```
uv add "mcp[cli]" httpx
uv pip install beautifulsoup4
```

4. Set your environment variables Create a .env file and add your Serper API key:
```
SERPER_API_KEY=your_serper_api_key
```

## 🧩 Claude Desktop Integration

To integrate this server as a tool within Claude Desktop:

Open Claude Desktop → File > Settings > Developer > Edit Config.

Update your claude_desktop_config.json to include the following:


```
{
    "mcpServers": {
        "documnetation": {
            "command": "uv",
            "args": [
                "--directory",
                "your_reository_where_the_repo_exists",
                "run",
                "main.py"
            ]

        }
    }
}
```


> 🔁 Important: Restart Claude Desktop after saving the config to load the new to

Once integrated successfully, you'll see your custom MCP tool appear within the Claude UI:


![image](https://github.com/user-attachments/assets/3a855889-c04c-49f1-a69a-61c3fdf9f1e8)


Use it to query docs in real time:

![MCP_tool_working](https://github.com/user-attachments/assets/5790241b-d94f-4fd9-ad26-cafd30933ca9)


![Working_MCP](https://github.com/user-attachments/assets/0d732017-52c4-41c5-8275-0a4c6f335609)



## 🪲Debugging in Real Time

One can also debug the tool that we created using the following command.

> Remember to install [NodeJs18+](https://nodejs.org/en/download)

```
npx @modelcontextprotocol/inspector uv run main.py
```
and follow to the port where the connection is setup.

![image](https://github.com/user-attachments/assets/965771df-3d1c-4f05-87e4-996e5a154d17)



## 🧰 Supported Libraries / Docs

![LangChain](https://img.shields.io/badge/LangChain-000000?style=for-the-badge&logo=chainlink&logoColor=white)

![LlamaIndex](https://img.shields.io/badge/LlamaIndex-8E44AD?style=for-the-badge&logo=llama&logoColor=white)

![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

More libraries can be easily added by updating the docs_urls dictionary.


## 🧠 Future Enhancements

- ✅ Add support for additional libraries like HuggingFace, PyTorch, TensorFlow, etc.

- ⚡ Implement caching to reduce redundant fetches and improve performance.

- 📈 Introduce a scoring/ranking mechanism based on relevance or token quality.

- 🧪 Unit testing and better exception handling for production readiness.
