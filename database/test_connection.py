import pyodbc
from db import build_conn_str, get_connection

def test_connection():
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        print("Connected successfully!")

        cursor.execute("SELECT @@VERSION")

        cursor.execute("""
        SELECT
            @@SERVERNAME AS ServerName,
            DB_NAME() AS DatabaseName,
            SUSER_SNAME() AS LoginName,
            GETDATE() AS CurrentTime
        """)

        row = cursor.fetchone()

        print("Server   :", row.ServerName)
        print("Database :", row.DatabaseName)
        print("Login    :", row.LoginName)
        print("Time     :", row.CurrentTime)

        conn.close()

    except Exception as e:
        print("Connection/test failed:")
        print(repr(e))

if __name__ == "__main__":
    test_connection()