import pandas as pd
from database.db import get_connection

def read_table(table_name):
    conn = get_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)

    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

    df = pd.DataFrame.from_records(rows, columns=columns)

    cursor.close()
    conn.close()

    return df