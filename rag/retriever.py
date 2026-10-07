from google import genai
import os
from rag.qdrant_connection import client
from qdrant_client.models import models
from dotenv import load_dotenv

load_dotenv(r"D:\CHATBOT\.env")

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

COLLECTION_NAME = "hm_products"

def retrieve_products(query: str, top_k: int = 10):

    result = gemini_client.models.embed_content(
        model="gemini-embedding-001",
        contents=query
    )

    query_vector = result.embeddings[0].values

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k
    ).points

    return results