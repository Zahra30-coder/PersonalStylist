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

try:
    with driver.session(database="neo4j") as session:

        print("Neo4j Version:")
        result = session.run("CALL dbms.components()")
        for record in result:
            print(record)

        print("\nDatabases:")
        result = session.run("""
            SHOW DATABASES
            YIELD name, currentStatus
            RETURN name, currentStatus
        """)

        for record in result:
            print(record["name"], record["currentStatus"])

finally:
    driver.close()