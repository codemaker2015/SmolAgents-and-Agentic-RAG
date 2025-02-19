# Importing OpenAI key
import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# Importing required libraries
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from smolagents import Tool
from smolagents import LiteLLMModel, DuckDuckGoSearchTool

# Loading the PDF
loader = PyPDFLoader("2404.14219v4.pdf")
pages = loader.load()
for page in pages:
    print(page.page_content)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
# split_document accepts a list of documents
splitted_docs = splitter.split_documents(pages) 

print(len(splitted_docs))
print(splitted_docs[0])
print(splitted_docs[1])
print(splitted_docs[2])

# Generate embeddings for the documents
embed_model = OpenAIEmbeddings(openai_api_key=openai_api_key)
embeddings = embed_model.embed_documents([chunk.page_content for chunk in splitted_docs])
print(f"Embeddings shape: {len(embeddings), len(embeddings[0])}")

vector_db = FAISS.from_documents(
    documents = splitted_docs,
    embedding = embed_model)

similar_docs = vector_db.similarity_search("What is Phi-3 training methodology", k=5)
print(similar_docs[0].page_content)


class RetrieverTool(Tool):
    name = "retriever"
    description = "Uses semantic search to retrieve the parts of the documentation that could be most relevant to answer your query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This should be semantically close to your target documents. Use the affirmative form rather than a question.",
            }
    }
    output_type = "string"
    def __init__(self, vector_db, **kwargs): # Add vector_db as an argument
        super().__init__(**kwargs)
        self.vector_db = vector_db # Store the vector database
    def forward(self, query: str) -> str:
        assert isinstance(query, str), "Your search query must be a string"
        docs = self.vector_db.similarity_search(query, k=4) # Perform search here
        return "\nRetrieved documents:\n" + "".join(
            [
                f"\n\n===== Document {str(i)} =====\n" + doc.page_content
                for i, doc in enumerate(docs)
            ]
        )
retriever_tool = RetrieverTool(vector_db=vector_db) # Pass vector_db during instantiation

model = LiteLLMModel(model_id="gpt-4o", api_key = openai_api_key)
search_tool = DuckDuckGoSearchTool()
from smolagents import CodeAgent
agent = CodeAgent(
    tools=[retriever_tool,search_tool], model=model, max_steps=6
)

agent_output = agent.run("Tell me about Microsoft")
print(agent_output)
agent_output = agent.run("What is Phi-3 training methodology")
print(agent_output)
agent_output = agent.run("Summarize technical specifications of Phi-3")
print(agent_output)

