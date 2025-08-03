# db.py
import sqlite3

DB_NAME = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row  # Optional: makes rows return dict-like
    return conn

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    sample_users = [
        ('John Doe', 'john@example.com', 'password123'),
        ('Jane Smith', 'jane@example.com', 'secret456'),
        ('Bob Johnson', 'bob@example.com', 'qwerty789')
    ]

    for name, email, password in sample_users:
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                (name, email, password)
            )

    conn.commit()
    conn.close()
    print("Database initialized with sample set of users.")

if __name__ == "__main__":
    initialize_db()
