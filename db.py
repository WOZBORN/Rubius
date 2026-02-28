import sqlite3

conn = sqlite3.connect("db.sqlite")
cur = conn.cursor()

def init_db():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS debts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        creditor TEXT NOT NULL,
        due_date TEXT,
        summa REAL NOT NULL CHECK(summa > 0)
    )
    """)
    conn.commit()

def add_debt(creditor: str, due_date: str, summa: float):
    cur.execute("""
    INSERT INTO debts (creditor, due_date, summa)
    VALUES (?, ?, ?)
    """, (creditor, due_date, summa))
    conn.commit()

def delete_debt(debt_id: int):
    cur.execute("""
    DELETE FROM debts
    WHERE id = ?
    """, (debt_id,))
    conn.commit()

def get_debts():
    cur.execute("""
    SELECT * FROM debts
    """)
    result = cur.fetchall()
    return result