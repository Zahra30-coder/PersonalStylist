#python -c "import os, requests; from dotenv import load_dotenv; load_dotenv(); u=os.getenv('QDRANT_CLUSTER_ENDPOINT'); k=os.getenv('QDRANT_API_KEY'); print('URL:',u); print('KEY:',bool(k)); r=requests.get(u+'/collections',headers={'api-key':k},timeout=30); print('STATUS:',r.status_code); print('RESPONSE:',r.text)"
#status: 200

from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv(r"D:\CHATBOT\.env")

parsed = urlparse("QDRANT_API_KEY")

print("Scheme:", repr(parsed.scheme))
print("Hostname:", repr(parsed.hostname))
print("Port:", repr(parsed.port))

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_CLUSTER_URL = os.getenv("QDRANT_CLUSTER_ENDPOINT")

print("URL:", repr(QDRANT_CLUSTER_URL))
print("API KEY EXISTS:", bool(QDRANT_API_KEY))

client = QdrantClient(
    url=QDRANT_CLUSTER_URL,
    api_key=QDRANT_API_KEY,
    timeout=10
)

print("Client created")

try:
    print("Testing connection...")
    result = client.get_collections()
    print("SUCCESS:")
    print(result)

except Exception as e:
    print("ERROR TYPE:", type(e).__name__)
    print("ERROR:", repr(e))
