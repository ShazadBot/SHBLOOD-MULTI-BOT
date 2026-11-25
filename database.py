
import sqlite3

DB = "shblood.db"

def connect():
    return sqlite3.connect(DB)

def setup():
    with connect() as db:
        db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT
        )
        """)

def add_user(user_id, username):
    with connect() as db:
        db.execute(
            "INSERT OR IGNORE INTO users VALUES (?, ?)",
            (user_id, username)
        )

def count_users():
    with connect() as db:
        return db.execute(
            "SELECT COUNT(*) FROM users"
        ).fetchone()[0]
