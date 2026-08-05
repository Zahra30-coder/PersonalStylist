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

driver = get_driver()

with driver.session(database="neo4j") as session:
    count = session.run("MATCH (n) RETURN count(n) AS c").single()["c"]
    print("Node count:", count)

driver.close()