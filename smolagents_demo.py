from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

# Choose which LLM engine to use
model = LiteLLMModel(model_id="gpt-4o", api_key = "YOUR_OPENAI_API_KEY")

# Create a code agent
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
agent.run("Tell me about Microsoft")