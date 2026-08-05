from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv(r"D:\CHATBOT\.env")

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(
        os.getenv("NEO4J_USERNAME"),
        os.getenv("NEO4J_PASSWORD")
    )
)

def get_driver():
    return driver