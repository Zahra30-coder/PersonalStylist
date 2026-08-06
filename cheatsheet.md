## Neo4j Cheat Sheet

| Task | Cypher Query |
|------|--------------|
| Total nodes | `MATCH (n) RETURN count(n);` |
| Total relationships | `MATCH ()-[r]->() RETURN count(r);` |
| Labels and node counts | `MATCH (n) RETURN labels(n), count(*) ORDER BY count(*) DESC;` |
| Relationship counts | `MATCH ()-[r]->() RETURN type(r), count(*) ORDER BY count(*) DESC;` |
| Graph visualization | `CALL db.schema.visualization();` |
| Sample graph | `MATCH (p)-[r]->(n) RETURN p, r, n LIMIT 100;` |
| Constraints | `SHOW CONSTRAINTS;` |
| Indexes | `SHOW INDEXES;` |
| Databases | `SHOW DATABASES;` |
| Product count | `MATCH (p:Product) RETURN count(p);` |
| View Departments | `MATCH (d:Department) RETURN d LIMIT 20;` |