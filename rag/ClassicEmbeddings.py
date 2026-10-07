import os

from dotenv import load_dotenv
from google import genai
from qdrant_client.models import Distance, VectorParams, PointStruct

from database.db import get_connection
from rag.qdrant_connection import client


load_dotenv(r"D:\CHATBOT\.env")

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# --------------------------------------------------
# Qdrant connection test
# --------------------------------------------------
print("Qdrant connected:")
print(client.get_collections())


# --------------------------------------------------
# Create collection if it doesn't exist
# --------------------------------------------------
collection_name = "hm_products"

collections = client.get_collections().collections

collection_exists = any(
    collection.name == collection_name
    for collection in collections
)

if not collection_exists:
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=3072,
            distance=Distance.COSINE
        )
    )

    print(f"Created collection: {collection_name}")

else:
    print(f"Collection already exists: {collection_name}")

# --------------------------------------------------
# Connect to Azure SQL
# --------------------------------------------------
conn = get_connection()
cursor = conn.cursor()

print("Database connected successfully!")

# --------------------------------------------------
# Fetch products
# --------------------------------------------------
cursor.execute("""
    SELECT TOP 500
        article_id,
        product_text
    FROM Products
    WHERE product_text IS NOT NULL
      AND LTRIM(RTRIM(product_text)) <> ''
""")

rows = cursor.fetchall()

print(f"Products fetched: {len(rows)}")

# --------------------------------------------------
# Generate embeddings
# --------------------------------------------------
points = []

for row in rows:

    article_id = int(row.article_id)
    product_text = row.product_text

    print(f"Embedding article: {article_id}")

    result = gemini_client.models.embed_content(
        model="gemini-embedding-001",
        contents=product_text
    )

    embedding = result.embeddings[0].values

    print(f"Embedding dimensions: {len(embedding)}")

    points.append(
        PointStruct(
            id=int(article_id),
            vector=embedding,
            payload={
                "article_id": int(article_id),
                "product_text": product_text
            }
        )
    )

# --------------------------------------------------
# Upload embeddings to Qdrant
# --------------------------------------------------
if points:

    client.upsert(
        collection_name=collection_name,
        points=points
    )

    print(f"Uploaded successfully: {len(points)} vectors")

# --------------------------------------------------
# Verify Qdrant
# --------------------------------------------------
count = client.count(
    collection_name=collection_name,
    exact=True
)

print(f"Qdrant points stored: {count.count}")

points = client.retrieve(
    collection_name="hm_products",
    ids=[888331006],
    with_vectors=True
)

print("ID:", points[0].id)
print("Vector dimensions:", len(points[0].vector))
print("First 10 values:", points[0].vector[:10])
print("Payload:", points[0].payload)

# --------------------------------------------------
# Close SQL connection
# --------------------------------------------------
cursor.close()
conn.close()

print("Done!")