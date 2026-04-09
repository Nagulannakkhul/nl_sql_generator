import tkinter as tk
from parser import generate_sql
from db import run_query

root = tk.Tk()
root.title("Natural Language to SQL Generator")

# Title
tk.Label(root, text="Enter Query:").pack()

# Input box
entry = tk.Entry(root, width=100)
entry.pack()

# SQL output
sql_label = tk.Label(root, text="", fg="blue")
sql_label.pack()

# Result output
result_label = tk.Label(root, text="", fg="green")
result_label.pack()

# Button function


def run():
    user_input = entry.get()

    sql_query = generate_sql(user_input)
    sql_label.config(text="SQL: " + sql_query)

    if "ERROR" in sql_query:
        result_label.config(text=sql_query)
    else:
        result = run_query(sql_query)

        if isinstance(result, str):
            result_label.config(text="Error: " + result)
        else:
            output = "\n".join(str(row) for row in result)
            result_label.config(text=output)


# Button
tk.Button(root, text="Run Query", command=run).pack()

root.mainloop()
