SYSTEM_PROMPT = """You are a helpful assistant with memory.

You have access to two types of memory:
- Facts (semantic): permanent knowledge about the user
- Events (episodic): past conversations and interactions

Use this context to give personalized, informed responses.
"""

def build_prompt(user_input: str, facts: list, events: list) -> str:
    context = ""
    if facts:
        context += "Facts I know:\n" + "\n".join(f"- {f}" for f in facts) + "\n\n"
    if events:
        context += "Past events:\n" + "\n".join(f"- {e}" for e in events) + "\n\n"
    return f"{context}User: {user_input}"