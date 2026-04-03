# 🧠 Omni Agent Lab

A conversational AI agent with **dual long-term memory** built on Llama 3.1, ChromaDB, and Sentence Transformers.

The agent remembers **facts** (semantic memory) and **past conversations** (episodic memory) — and uses both to give personalized, context-aware responses.

---

## How It Works

| Memory Type | What It Stores | Example |
|---|---|---|
| **Semantic** | Permanent facts about the user | "User is allergic to peanuts" |
| **Episodic** | Past conversations, time-stamped | "Tuesday: discussed Q3 budget" |

When you send a message, the agent searches both memory stores, injects the most relevant results into the prompt, and sends everything to Llama 3.1.

---

## Project Structure

```
omni_agent_lab/
├── main.py                  # Entry point — run this
├── core/
│   ├── memory_engine.py     # BaseMemory, SemanticMemory, EpisodicMemory
│   └── agent.py             # Agent class — coordinates memory + LLM
└── utils/
    └── prompts.py           # System prompt + prompt builder
```

---

## Requirements

- Python 3.9+
- [Ollama](https://ollama.com) installed and running locally with Llama 3.1

---

## Installation

**1. Clone the repo**
```bash
git clone https://github.com/your-username/omni-agent-lab.git
cd omni-agent-lab
```

**2. Install dependencies**
```bash
pip install chromadb sentence-transformers ollama
```

**3. Pull Llama 3.1 via Ollama**
```bash
ollama pull llama3.1
```

**4. Run the agent**
```bash
python main.py
```

---

## Usage

Once running, just type your message and press Enter. Type `exit` to quit.

```
You: What should I avoid eating?
Agent: Based on what I know, you are allergic to peanuts so you should avoid...

You: What did we talk about last week?
Agent: Last Tuesday we discussed the Q3 marketing budget...
```

To seed facts and past events, edit `main.py`:

```python
# Add a permanent fact
agent.semantic.remember("User is vegetarian", "diet-001")

# Add a past event
agent.episodic.remember("Monday: user asked about meal planning")
```

---

## Tech Stack

- **[Llama 3.1](https://ollama.com/library/llama3.1)** via Ollama — local LLM
- **[ChromaDB](https://www.trychroma.com)** — vector database for both memory stores
- **[Sentence Transformers](https://www.sbert.net)** — `all-MiniLM-L6-v2` embedding model

---

## License

MIT
