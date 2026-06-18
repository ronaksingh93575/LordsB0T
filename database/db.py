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
        ("Killerboat", "1234"),
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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
                   username TEXT PRIMARY KEY,

                   check_shield INTEGER DEFAULT 0,
                   auto_colosseum INTEGER DEFAULT 0,
                   auto_gathering INTEGER DEFAULT 0,
                   auto_training INTEGER DEFAULT 0,
                   auto_healing INTEGER DEFAULT 0,
                   auto_collecting INTEGER DEFAULT 0
                   )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS account_status(
                   username TEXT PRIMARY KEY,
                   shield_active INTEGER DEFAULT 0,
                   shield_time TEXT,
                   last_updated TEXT)

    """)

    #default settings
    default_settings = [
        ("Killerboat",),
        ("ronak",),
        ("almighty",)
    ]

    cursor.executemany(
        """
        INSERT OR IGNORE INTO settings(username)
        values(?)
        """,
        default_settings
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


def get_user_settings(username):

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT
        check_shield,
        auto_colosseum,
        auto_gathering,
        auto_training,
        auto_healing,
        auto_collecting
        
        FROM settings
        WHERE username=?
        """,
        (username,)
    )
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "check_shield": (row[0]),
            "auto_colosseum": (row[1]),
            "auto_gathering": (row[2]),
            "auto_training": (row[3]),
            "auto_healing": (row[4]),
            "auto_collecting": (row[5])
        }
    return None

def save_settings(
        username,
        check_shield,
        auto_colosseum,
        auto_gathering,
        auto_training,
        auto_healing,
        auto_collecting
):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE settings
        SET
        check_shield=?,
        auto_colosseum=?,
        auto_gathering=?,
        auto_training=?,
        auto_healing=?,
        auto_collecting=?
        WHERE username=?
        """,
        (
            check_shield,
            auto_colosseum,
            auto_gathering,
            auto_training,
            auto_healing,
            auto_collecting,
            username
        )
    )

    conn.commit()
    conn.close()

def update_shield_status(
        username,
        shield_active,
        shield_time
):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO account_status(
            username,
            shield_active,
            shield_time,
            last_updated
        )

        VALUES(
            ?,
            ?,
            ?,
            datetime('now')
        )
        """,
        (
            username,
            shield_active,
            shield_time
        )
    )

    conn.commit()

    conn.close()


def get_shield_status(username):

    conn = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
        shield_active,
        shield_time

        FROM account_status

        WHERE username=?
        """,
        (username,)
    )

    row = cursor.fetchone()

    conn.close()

    return row


if __name__ == "__main__":

    create_database()

    # Example:
    # add_user("newuser", "9999")

    print("Database created successfully.")

