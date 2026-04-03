from core.memory_engine import SemanticMemory, EpisodicMemory
from utils.prompts import SYSTEM_PROMPT, build_prompt
from ollama import Client

class Agent:
    def __init__(self):
        self.semantic = SemanticMemory()
        self.episodic = EpisodicMemory()
        self.llm = Client()

    def chat(self, user_input: str) -> str:
        facts = self.semantic.search(user_input)
        events = self.episodic.search(user_input)

        prompt = build_prompt(user_input, facts, events)

        response = self.llm.chat(
            model="llama3.1",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": prompt},
            ]
        )

        # Save this exchange to episodic memory
        self.episodic.remember(f"User asked: {user_input}")

        return response["message"]["content"]