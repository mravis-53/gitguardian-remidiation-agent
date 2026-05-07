from agent.llm_agent import LLMAgent

def test_agent_response():
    agent = LLMAgent()
    result = agent.suggest_fix("API_KEY = '123'")
    assert result is not None
