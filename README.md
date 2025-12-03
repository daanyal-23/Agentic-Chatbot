# 🤖 Agentic Chatbot Platform  
A modular, agent-driven conversational AI system built using **LangChain**, **LangGraph**, **Streamlit**, and **LLMs (Groq/HuggingFace)**.  
This project demonstrates how an LLM can behave as an **intelligent agent** — capable of routing queries, calling tools, retrieving information, maintaining memory, and generating refined responses.

---

## 🧩 How It Works

The Agentic Chatbot follows an **agent-based workflow** consisting of:

### **1️⃣ Router Agent**  
Classifies the user query and decides the next best action:  
- Use LLM directly  
- Trigger a tool call  
- Perform retrieval  
- Ask for clarification

### **2️⃣ Retrieval Agent (Optional)**  
Fetches relevant context when the query requires external information.

### **3️⃣ Tool Agent**  
Handles external tool calls such as:  
- Web search  
- Calculation  
- Utilities (formatting, conversions, etc.)

### **4️⃣ LLM Answer Agent**  
Generates a natural, coherent answer using Gemma/Groq/HuggingFace LLMs.

### **5️⃣ Memory & Logging**  
Conversation context, tool traces, and decision flow are stored for improved continuity.

### **6️⃣ Streamlit UI**  
Provides a clean, interactive chat interface showing:  
✔ user messages  
✔ agent decisions  
✔ tool usage  
✔ final LLM outputs  

---

## 🚀 Features

- 🧠 **Agentic Routing** — intelligently chooses the correct workflow path  
- 🔧 **Tool Calling** — search, utilities, or custom tool integrations  
- 🔄 **Query Understanding** — classifies intent before responding  
- 📚 **Optional Retrieval Integration** — fetch documents when needed  
- 🤖 **Low-latency LLM Generation** — via Groq or HuggingFace  
- 🧵 **Memory Support** — maintains chat history  
- 📊 **UI Transparency** — shows which agent acted and why  
- ⚡ **Fast, lightweight Streamlit interface**

---

## 📂 Project Structure
```bash
Agentic-Chatbot/
│
├── app.py # Streamlit UI entrypoint
├── main.py # Backend or graph testing entrypoint
├── requirements.txt # Dependencies
├── README.md # Documentation
├── .env.example # API key template
│
├── src/
│ ├── agents/ # Core agent modules
│ │ ├── router_agent.py
│ │ ├── tool_agent.py
│ │ ├── retrieval_agent.py
│ │ └── llm_agent.py
│ │
│ ├── graph/ # LangGraph workflow
│ │ └── workflow.py
│ │
│ ├── tools/ # External tools
│ │ ├── search_tool.py
│ │ └── utils.py
│ │
│ └── state/ # Shared graph or conversation state
│ └── agent_state.py
│
└── UI/
└── streamlitUI/
├── display_result.py
├── loadui.py
└── uiconfigfile.py
```

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/daanyal-23/Agentic-Chatbot.git
cd Agentic-Chatbot
```
2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
```bash
source venv/bin/activate
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Configure Environment Variables
Create a .env file:

GROQ_API_KEY=your_groq_api_key
HUGGINGFACE_API_KEY=your_hf_api_key
LANGSMITH_API_KEY=optional
5️⃣ Run the Streamlit App
```bash
streamlit run app.py
```
🧪 Example Workflow
User enters a message in the Streamlit chat.

Router Agent analyzes query intent.

Depending on the type of query, the router may:

Directly call the LLM

Invoke a tool

Perform retrieval

The appropriate agent handles execution.

LLM Agent generates a final answer.

UI displays the full reasoning chain, including tool calls.

📌 Future Improvements
🔍 Add Retrieval-Augmented Generation (RAG) integration

📊 Add chat analytics and session metrics

🧪 Add unit tests for agent decision logic

🐳 Containerize with Docker

🧠 Add memory persistence (Redis/SQLite)

🧩 Extend with domain-specific tools (medical, finance, etc.)

📈 Add LangSmith evaluation dashboard

🤝 Contributing
PRs are welcome!
For major changes, please open an issue to discuss the proposal before implementation.

❤️ Built With
LangChain – agent tools & LLM orchestration

LangGraph – workflow routing

Streamlit – interactive UI

Groq / HuggingFace LLMs – fast inference

Python – backend logic
