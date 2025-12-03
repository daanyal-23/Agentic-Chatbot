# 🛠️ Corrective RAG  
A fully modular **Corrective Retrieval-Augmented Generation (RAG)** pipeline built using **LangGraph**, **Streamlit**, and **Groq LLMs**.

This project demonstrates an advanced RAG system that **retrieves, grades, refines, and augments context** before generating an answer — significantly improving reliability compared to standard single-pass RAG.

---

## 🧩 How It Works

The **Corrective RAG pipeline** follows these intelligent steps:

### **1️⃣ Retrieve**  
Fetch candidate documents from the local knowledge base.

### **2️⃣ Grade**  
Evaluate each retrieved document to determine how relevant it is to the user’s query.

### **3️⃣ Transform**  
If the retrieval quality is poor, automatically **rewrite** the user query using an LLM to get better retrieval results.

### **4️⃣ Web Search (Fallback)**  
If domain knowledge is missing, trigger an **external search** (e.g., Tavily API) to bring in fresh information.

### **5️⃣ Generate**  
Use **Groq-hosted LLMs** to produce the final answer using the best available context.

### **6️⃣ UI Feedback**  
The **Streamlit frontend** displays each workflow step:
- Retrieved docs  
- Relevance grades  
- Rewritten queries  
- Web search results  
- Final generated answer  

This provides complete **transparency of the reasoning pipeline**.

---

## 🚀 Features

- 📄 **Document Retrieval & Grading**  
  Retrieves documents and filters them based on relevance.

- 🔄 **Automatic Query Transformation**  
  Rewrites user questions when retrieval is weak.

- 🌐 **Web Search Fallback**  
  Adds missing or new knowledge when necessary.

- 🤖 **LLM-Powered Answer Generation**  
  Uses Groq-hosted LLMs for fast, low-latency inference.

- 📊 **Execution Logs in UI**  
  Transparent end-to-end visualization of:  
  `retrieve → grade → transform → search → generate`

---

## 📂 Project Structure
```bash
CorrectiveRAG/
│
├── app.py # Streamlit app (UI entrypoint)
├── main.py # CLI runner for workflow debugging
├── requirements.txt # Dependencies
├── README.md # Documentation
├── .env.example # Environment variable template
│
├── src/
│ ├── langgraphCorrectiveAI/
│ │ ├── graph/
│ │ │ └── workflow.py # Core workflow graph
│ │ │
│ │ ├── nodes/ # Workflow nodes
│ │ │ ├── retrieve_node.py
│ │ │ ├── grade_node.py
│ │ │ ├── transform_node.py
│ │ │ ├── web_search_node.py
│ │ │ └── generate_node.py
│ │ │
│ │ ├── tools/
│ │ │ └── search_tool.py # Embeddings, retrieval, search utilities
│ │ │
│ │ └── state/
│ │ └── graph_state.py # Shared workflow state
│ │
│ └── UI/streamlitUI/
│ ├── display_result.py
│ ├── loadui.py
│ └── uiconfigfile.py
```

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/daanyal-23/corrective-rag-demo.git
cd corrective-rag-demo
```
2️⃣ Create a Virtual Environment
```bash
Copy code
python -m venv venv
Windows
```
```bash
Copy code
venv\Scripts\activate
Mac/Linux
```
```bash
Copy code
source venv/bin/activate
```
3️⃣ Install Dependencies
```bash
Copy code
pip install -r requirements.txt
```
4️⃣ Configure Environment Variables
Create a .env file in the project root:

Copy code
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
(You may also include any embedding model keys if needed.)

5️⃣ Run the Streamlit App
```bash
streamlit run app.py
```
🧪 Example Workflow
Enter a question in the Streamlit interface.

System retrieves documents and grades relevance.

If retrieval is poor, query is rewritten for improvement.

If required, external web search is triggered.

Groq LLM generates the final, grounded answer.

UI shows each step with explanations.

📌 Future Improvements
✅ Add unit tests for workflow nodes

✅ Enhance frontend visualization

✅ Add multi-vector-store support (FAISS, Pinecone, Chroma)

✅ Dockerize for easier deployment

⏳ Add evaluator agent for grounding verification

⏳ Add streaming output support in UI

🤝 Contributing
Contributions are welcome!
Please open an issue before submitting major changes so we can discuss your ideas.

❤️ Built With
LangGraph – workflow orchestration

Groq LLMs – fast inference

Streamlit – interactive frontend

Python – glue for all components
