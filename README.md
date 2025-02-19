# SmolAgents & Agentic RAG

SmolAgents is a lightweight agent framework developed by Hugging Face, designed for building AI agents with minimal complexity while maintaining flexibility. It enables the creation of autonomous agents that can reason, retrieve information, and execute code dynamically. 

Agentic RAG (Retrieval-Augmented Generation) extends this capability by integrating retrieval-based information retrieval with LLM-driven reasoning, enabling AI systems to provide more accurate, contextual, and up-to-date responses.

## Features

- **Minimalist Framework**: SmolAgents simplifies agent development with minimal abstraction.
- **Code Agents**: Executes Python code for dynamic computation and tool use.
- **Tool-Based Reasoning**: Integrates external tools such as search engines and databases.
- **Secure Execution**: Runs code in sandboxed environments for safety.
- **Retrieval-Augmented Generation (RAG)**: Combines LLM-based reasoning with real-time information retrieval.

## Installation

- Clone the repository:
  ```sh
  git clone https://github.com/codemaker2015/SmolAgents-and-Agentic-RAG.git
  cd AgenticRAG
  ```

- Create a virtual environment (optional but recommended):
  ```sh
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```

- To set up the environment, install the dependencies:

  ```sh
  pip install -r requirements.txt
  ```
## Environment Variables
Create a .env file in the project root to store API keys and other secrets. A sample .env file might look like:

```sh
OPENAI_API_KEY=your_openai_key
HUGGINGFACE_API_KEY=your_huggingface_key
```
## Usage
- Running the Agentic RAG Demo
  The agentic_rag_demo.py script demonstrates an AI agent retrieving and reasoning over documents.
  ```sh
  python agentic_rag_demo.py
  ```
- Running the SmolAgents Demo
  The smolagents_demo.py script showcases a basic SmolAgent in action.
  ```sh
  python smolagents_demo.py
  ```
- Task-Oriented Agent
  A more structured agent can be tested using:
  ```sh
  python task_oriented_agent_demo.py
  ```
## How It Works
- **Loading Data**: The system processes PDFs and text files, extracting relevant content.
- **Generating Embeddings**: Documents are split into chunks and transformed into vector embeddings.
- **Storing in FAISS**: The FAISS vector database is used for efficient retrieval.
- **Query Execution**: The agent takes user queries and finds relevant information using RAG.
- **Tool Integration**: The agent may also use external tools (e.g., web search) to enrich responses.