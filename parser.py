from db import get_tables, get_columns
import re

def generate_sql(user_input):
    text = user_input.lower()

    tables = get_tables()

    # find table name in user input
    table = None
    for t in tables:
        if t in text:
            table = t
            break

    # if no table found → use first table
    if not table:
        table = tables[0]

    columns = get_columns(table)

    # DEFAULT SELECT
    if "all" in text:
        return f"SELECT * FROM {table};"

    # TOP N logic
    if "top" in text:
        match = re.search(r'\d+', text)
        limit = match.group() if match else "5"

        # find numeric column (simple logic)
        col = columns[-1]  # last column (assume numeric)

        return f"""
        SELECT {columns[1]}, SUM({col})
        FROM {table}
        GROUP BY {columns[1]}
        ORDER BY SUM({col}) DESC
        LIMIT {limit};
        """

    return "ERROR: Query not supported"