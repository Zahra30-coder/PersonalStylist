from math import ceil

def import_relationships(
    driver,
    dataframe,
    source_label,
    source_key,
    target_label,
    target_key,
    fk_column,
    relationship,
    batch_size=1000,
):
    query = f"""
    UNWIND $rows AS row

    MATCH (a:{source_label} {{{source_key}: row.{source_key}}})
    MATCH (b:{target_label} {{{target_key}: row.{fk_column}}})

    MERGE (a)-[r:{relationship}]->(b)
    """
    rows = dataframe.to_dict("records")
    total = len(rows)

    with driver.session(database="neo4j") as session:

        for i in range(0, total, batch_size):
            batch = rows[i:i + batch_size]
            session.run(query, rows=batch).consume()
            print(
                f"{relationship}: "
                f"{min(i + batch_size, total)}/{total}"
            )
    print(f"✓ {relationship} completed ({total} relationships)")
    return total

