from neo4j import GraphDatabase


def import_nodes(driver, label, primary_key, dataframe):

    properties = dataframe.columns.tolist()

    set_clause = ", ".join(
        [f"n.{col} = ${col}" for col in properties]
    )

    query = f"""
    MERGE (n:{label} {{{primary_key}: ${primary_key}}})

    SET {set_clause}
    """

    with driver.session(database="neo4j") as session:

        for row in dataframe.to_dict("records"):

            session.run(query, **row)

    print(f"{label} imported")