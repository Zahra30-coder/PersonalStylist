# 👗 AI Personal Stylist

An end-to-end **Generative AI Personal Stylist** that provides personalized outfit recommendations by combining **Azure SQL**, **Neo4j**, **Azure AI Search**, **LlamaIndex**, and **Google Gemini**.

The application leverages a **Hybrid Retrieval-Augmented Generation (RAG)** architecture to deliver context-aware, explainable, and personalized fashion recommendations based on user preferences, body type, skin tone, occasion, weather, and product relationships.

---

# 🚀 Features

* 🤖 AI-powered outfit recommendations
* 💬 Multi-turn conversational chatbot
* 👤 Personalized user profiles
* 👗 Occasion-based outfit suggestions
* ☀️ Weather-aware recommendations
* 🎨 Skin tone and color matching
* 📐 Body shape recommendations
* 🔍 Hybrid semantic + structured search
* 🧠 Graph-based outfit matching
* 📝 Explainable recommendations
* 📊 Langfuse observability
* ⚡ FastAPI REST APIs

---

# 🏗️ Architecture

```text
                                     User
                                       │
                                       ▼
                               FastAPI Backend
                                       │
                                       ▼
                        LangGraph Agent / Orchestrator
                                       │
             ┌─────────────────────────┴────────────────────────┐
             ▼                                                  ▼
     Conversation Memory                              Entity Extraction
             │                                                  │
             └─────────────────────────┬────────────────────────┘
                                       ▼
                           LlamaIndex Query Engine
                                       │
          ┌───────────────┬────────────┴────────────┬───────────────┐
          ▼               ▼                         ▼               ▼
   Azure SQL       Azure AI Search           Neo4j Graph       External APIs
 (Metadata)      (Vector Retrieval)       (GraphRAG)      (Weather, Trends)
          │               │                         │               │
          └───────────────┴────────────┬────────────┴───────────────┘
                                       ▼
                           Hybrid Context Fusion
                                       │
                                       ▼
                          Cross-Encoder Reranker
                                       │
                                       ▼
                     Prompt Builder + Grounding Layer
                                       │
                                       ▼
                             Gemini 2.5 Flash
                                       │
                                       ▼
                        Structured AI Recommendation
                                       │
              ┌────────────────────────┴─────────────────────────┐
              ▼                                                  ▼
        Langfuse Tracing                              RAG Evaluation
    (Latency • Tokens • Cost)             (Faithfulness • Recall • Precision)
```

# 🏗️ User UI

```
                            User
                              │
                              ▼
                       FastAPI Backend
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
      User Profile Store          Conversation Memory
 (Body Shape • Skin Tone •        (Chat History)
  Size • Budget • Preferences)
                └─────────────┬─────────────┘
                              ▼
                     Retrieval Pipeline
```

# 🏗️ Graph RAG Setup

```
1. Clean Dataset
        │
        ▼
2. Normalize SQL Database
        │
        ▼
3. Create SQL Foreign Keys
        │
        ▼
4. Design Graph Schema
        │
        ▼
5. Create Neo4j Constraints
        │
        ▼
6. Import Nodes (UNWIND + MERGE)
        │
        ▼
7. Verify Labels
        │
        ▼
8. Import Relationships
        │
        ▼
9. Verify Relationship Counts
        │
        ▼
10. Visualize Graph
        │
        ▼
11. Build GraphRAG Retriever
```
---

# 🛠️ Tech Stack

## Backend

* Python
* FastAPI

## AI / LLM

* Google Gemini
* LlamaIndex
* RAG

## Databases

* Azure SQL Database
* Neo4j

## Search

* Azure AI Search
* Vector Search
* Semantic Search
* Hybrid Search

## AI Components

* Embeddings
* HNSW
* Cross Encoder Reranking
* Context Fusion

## Monitoring

* Langfuse

---

# 🕸️ Neo4j Graph

Example relationships:

* `MATCHES_WITH`
* `SIMILAR_TO`
* `SUITABLE_FOR`
* `BELONGS_TO`
* `HAS_COLOR`
* `OCCASION`
* `STYLE`

---

# 🔄 AI Retrieval Pipeline

1. User submits a query.
2. FastAPI receives the request.
3. LlamaIndex routes the query.
4. Azure SQL performs structured filtering.
5. Azure AI Search performs semantic retrieval.
6. Neo4j expands product relationships.
7. Context Fusion merges retrieved information.
8. Cross-Encoder reranks the retrieved context.
9. Gemini generates the final recommendation.

---

# 👗 Recommendation Factors

* Body Shape
* Skin Tone
* Favorite Colors
* Style Preference
* Occasion
* Weather
* Season
* Budget
* Conversation History
* Purchase History

---

# ⚙️ Installation

Creating Neo4j Nodes and Relationships
```bash
python -m venv graph.run_imports
```
IMPORT_NODES = False
IMPORT_RELATIONSHIPS = True

Set variables according to what you are trying to achieve

Create a virtual environment.

```bash
python -m venv chatbot-env
```

Activate the environment.

### Windows

```bash
chatbot-env\Scripts\activate
```

### Linux / macOS

```bash
source chatbot-env/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
uvicorn app.main:app --reload
```




