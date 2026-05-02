# 🔍 Search-Augmented AI Agent (ReAct-based)

An autonomous AI agent built from scratch (without frameworks) that combines LLM reasoning with real-time web search to answer queries beyond its knowledge cutoff.


##  Overview

This project implements a **ReAct-style agent loop** where an LLM can:

- Decide when it needs external information  
- Call a search tool dynamically  
- Process retrieved data  
- Generate a final answer  

The system follows an iterative reasoning loop:

User → LLM → Action (Search) → Observation → LLM → Final Answer  



##  Key Features

-  **ReAct Agent Architecture**  
  Implements multi-step reasoning using Action → Observation → Answer loop  

-  **Search-Augmented Generation**  
  Integrates real-time web search (Serper API) to overcome LLM knowledge limitations  

-  **Modular Design**
  - LLM interface (`client.py`)
  - Agent loop (`main.py`)
  - Memory (`memory.py`)
  - Prompt control (`prompt.py`)
  - Tool layer (`tool.py`)

-  **Prompt Engineering**
  - Strict structured outputs (Action / Input / Final Answer)
  - Controlled agent behavior
  - Prevents infinite loops via explicit rules  

-  **Contextual Memory**
  Maintains conversation history for multi-turn reasoning  

-  **Custom Tool Invocation**
  Parses unstructured LLM outputs into executable actions  



##  How It Works

1. User inputs a query  
2. LLM decides:
   - Answer directly OR  
   - Call search tool  
3. If search is called:
   - Query is sent to Serper API  
   - Results are cleaned and formatted  
4. Results are fed back as **Observation**  
5. LLM generates final answer  