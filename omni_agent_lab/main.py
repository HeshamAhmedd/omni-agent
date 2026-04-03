from core.agent import Agent

agent = Agent()


agent.semantic.remember("The user is allergic to peanuts", "allergy-001")
agent.semantic.remember("The user works in marketing", "job-001")


agent.episodic.remember("Last Tuesday we discussed the Q3 marketing budget")

# Chat
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = agent.chat(user_input)
    print(f"Agent: {response}\n")