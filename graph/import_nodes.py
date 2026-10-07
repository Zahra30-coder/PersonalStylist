from math import ceil
def import_nodes(driver, label, primary_key, dataframe, batch_size=1000):

    query = f"""
    UNWIND $rows AS row
    MERGE (n:{label} {{{primary_key}: row.{primary_key}}})
    SET n += row
    """

    rows = dataframe.to_dict("records")
    total = len(rows)

    with driver.session(database="neo4j") as session:

        for i in range(0, total, batch_size):

            batch = rows[i:i + batch_size]

            # THIS IS THE MISSING LINE
            session.run(query, rows=batch).consume()

            print(f"{label}: Imported {min(i + batch_size, total)}/{total}")

    print(f"✓ {label} import completed ({total} records)")

    return total