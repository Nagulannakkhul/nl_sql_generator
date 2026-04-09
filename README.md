# 🧠 Natural Language to SQL Query Generator

## 📌 Overview

The **Natural Language to SQL Query Generator** is a desktop-based application that converts simple English queries into SQL statements and executes them on a PostgreSQL database.

This project is built using **Python**, **PostgreSQL**, and **Tkinter**, and follows a **rule-based approach** (without using AI/ML models).

---

## 🎯 Objective

To simplify database interaction by allowing users to query data using natural language instead of writing SQL manually.

---

## 🚀 Key Features

* 🔹 Convert natural language → SQL queries
* 🔹 Execute queries directly on PostgreSQL
* 🔹 Dynamic table and column detection
* 🔹 Supports basic operations:

  * SELECT
  * WHERE
  * GROUP BY
  * ORDER BY
  * LIMIT (Top N queries)
* 🔹 Simple and user-friendly GUI (Tkinter)
* 🔹 No external APIs (fully offline system)

---

## 🛠️ Technologies Used

* **Python** – Core programming language
* **PostgreSQL** – Database management system
* **Tkinter** – GUI development
* **psycopg2** – Python-PostgreSQL connector

---

## 📂 Project Structure

```
nl_sql_project/
│
├── app.py        # GUI application (main file)
├── parser.py     # Natural language to SQL conversion logic
├── db.py         # Database connection and query execution
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
https://github.com/Nagulannakkhul/nl_sql_generator.git
cd nl_sql_generator
```

---

### 2️⃣ Install Dependencies

```bash
pip install psycopg2
```

---

### 3️⃣ Database Setup (PostgreSQL)

Create database:

```sql
CREATE DATABASE project_db;
```

Create table:

```sql
CREATE TABLE sales (
    order_id SERIAL PRIMARY KEY,
    customer_name TEXT,
    product TEXT,
    amount INT,
    city TEXT
);
```

Insert sample data:

```sql
INSERT INTO sales (customer_name, product, amount, city) VALUES
('John', 'Laptop', 50000, 'Chennai'),
('Alice', 'Phone', 20000, 'Mumbai'),
('Bob', 'Tablet', 15000, 'Delhi'),
('John', 'Phone', 18000, 'Chennai'),
('Alice', 'Laptop', 55000, 'Mumbai');
```

---

### 4️⃣ Configure Database Connection

Edit `db.py`:

```python
password = "your_password"
```

---

### 5️⃣ Run Application

```bash
python app.py
```

---

## 💡 Example Queries

| Natural Language Input | Description            |
| ---------------------- | ---------------------- |
| `all`                  | Show all records       |
| `top 3 customers`      | Top customers by sales |
| `total sales by city`  | Grouped sales data     |
| `chennai`              | Filter by city         |

---

## ⚠️ Limitations

* Rule-based system (no advanced NLP understanding)
* Supports limited query patterns
* Assumes predefined database structure

---

## 🔮 Future Enhancements

* AI/LLM-based query understanding
* Support for complex joins
* Interactive table view (grid format)
* Web-based version (Flask/React)

---

## 👨‍💻 Author

* https://github.com/Nagulannakkhul

---

## 📌 Conclusion

This project demonstrates how natural language can be translated into SQL queries using rule-based logic, making databases more accessible for non-technical users.

---

⭐ If you like this project, feel free to star the repository!
