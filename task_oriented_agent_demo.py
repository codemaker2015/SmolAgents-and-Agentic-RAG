from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
import yfinance as yf

# Initialize the LLM model with the corrected string for the API key
model = LiteLLMModel(model_id="gpt-4o", api_key = "YOUR_OPENAI_API_KEY")

# Define the agent with tools and imports
agent = CodeAgent(
   tools=[DuckDuckGoSearchTool()],
   additional_authorized_imports=["yfinance"],
   model=model
)
# Run the agent to fetch the stock price of Apple Inc.
response = agent.run(
   "Fetch the stock price of Microsoft Inc (NASDAQ: AAPL). Use the YFinance Library."
)
# Output the response
print(response)