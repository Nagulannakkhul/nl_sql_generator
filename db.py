import psycopg2

# Run query


def run_query(query):
    try:
        conn = psycopg2.connect(
            dbname="nl_project_db",
            user="postgres",
            password=input("Enter DB password: "),
            host="localhost",
            port="5432"
        )

        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()

        conn.close()
        return rows

    except Exception as e:
        return str(e)


# Get all table names
def get_tables():
    conn = psycopg2.connect(
        dbname="nl_project_db",
        user="postgres",
        password=input("Enter DB password: "),
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public';
    """)

    tables = [row[0] for row in cur.fetchall()]
    conn.close()

    return tables


# Get column names of a table
def get_columns(table_name):
    conn = psycopg2.connect(
        dbname="nl_project_db",
        user="postgres",
        password=input("Enter DB password: "),
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute(f"""
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name = '{table_name}';
    """)

    columns = [row[0] for row in cur.fetchall()]
    conn.close()

    return columns
