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
                     FastAPI API
                          │
                          ▼
                Conversation Memory
                          │
                          ▼
                 LlamaIndex Router
              ┌───────────┴───────────┐
              ▼                       ▼
      Azure SQL Database      Azure AI Search
     (Structured Search)     (Semantic Search)
              │                       │
              └───────────┬───────────┘
                          ▼
                    Neo4j Graph
               (Relationship Search)
                          │
                          ▼
                    Context Fusion
                          │
                          ▼
                Cross-Encoder Reranker
                          │
                          ▼
                     Gemini 2.5 Flash
                          │
                          ▼
              AI Outfit Recommendation
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

# 📂 Project Structure

```text
app/
│
├── api/
├── database/
│   ├── db.py
│   ├── create_tables.py
│   ├── load_data.py
│   └── test_connection.py
│
├── graph/
├── indexing/
├── llm/
├── retrieval/
├── observability/
├── models/
├── utils/
└── main.py

data/
│
├── articles.csv
├── customers.csv
└── transactions.csv
```

---

# 🗄️ Database Schema

The product catalog is normalized into multiple relational tables.

* Products
* Product Types
* Departments
* Sections
* Garment Groups
* Colors
* Graphical Appearance
* Perceived Color Value
* Perceived Color Master
* Index
* Index Group

All entities are connected using foreign keys to maintain referential integrity.

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

# 🌐 API Endpoints

### Chat

```http
POST /chat
```

### Products

```http
GET /products
```

### Product Search

```http
GET /products/search
```

### User Profile

```http
POST /profile
```

---

# ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/<username>/<repository>.git
```

Navigate to the project.

```bash
cd AI-Personal-Stylist
```

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

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

```env
# Azure SQL
DB_SERVER=
DB_NAME=
DB_DRIVER=ODBC Driver 18 for SQL Server
AZURE_SQL_USER=
DB_PASSWORD=

# Neo4j
NEO4J_URI=
NEO4J_USERNAME=
NEO4J_PASSWORD=

# Azure AI Search
AZURE_SEARCH_ENDPOINT=
AZURE_SEARCH_KEY=
AZURE_SEARCH_INDEX=

# Gemini
GOOGLE_API_KEY=

# Langfuse
LANGFUSE_PUBLIC_KEY=
LANGFUSE_SECRET_KEY=
LANGFUSE_BASE_URL=
```

---

# 🔮 Future Enhancements

* Image-based outfit recommendations
* Virtual Try-On
* Personal wardrobe management
* Fashion trend prediction
* Voice assistant
* Mobile application
* Recommendation evaluation using RAGAS
* Agentic workflows
* Azure deployment
* CI/CD pipeline

---

# 📜 License

This project is licensed for educational, research, and portfolio purposes.
