from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel

# Choose Together based DeepSeek model to use
model = OpenAIServerModel(
    model_id="deepseek-ai/DeepSeek-R1",
    api_base="https://api.together.xyz/v1/", # Leave this blank to query OpenAI servers.
    api_key="YOUR_TOGETHER_API_KEY", # Switch to the API key for the server you're targeting.
)

# Create a code agent
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
agent.run("Tell me about Microsoft")