import os
import openai

class LLMAgent:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def suggest_fix(self, vulnerability_context: str) -> str:
        prompt = f"""
You are a secure coding assistant.
Fix the following security issue and return only corrected code.

Issue:
{vulnerability_context}
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content
