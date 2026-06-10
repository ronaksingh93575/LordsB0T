import sqlite3
import os

DATABASE_PATH = "database/users.db"


def create_database():
    """
    Create database and users table if they do not exist.
    """

    # Create database folder if missing
    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Default users
    default_users = [
        ("Ki11erB0AT", "1234"),
        ("ronak", "1234"),
        ("almighty", "1234")
    ]

    cursor.executemany(
        """
        INSERT OR IGNORE INTO users(username, password)
        VALUES(?, ?)
        """,
        default_users
    )

    conn.commit()
    conn.close()


def authenticate_user(username, password):

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def add_user(username, password):

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users(username, password)
            VALUES(?, ?)
            """,
            (username, password)
        )

        conn.commit()
        print(f"User '{username}' added successfully.")

    except sqlite3.IntegrityError:
        print("Username already exists.")

    finally:
        conn.close()


if __name__ == "__main__":

    create_database()

    # Example:
    # add_user("newuser", "9999")

    print("Database created successfully.")