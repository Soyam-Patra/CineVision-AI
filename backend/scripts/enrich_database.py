from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[2]

DB = ROOT / "backend" / "movies.db"

conn = sqlite3.connect(DB)
cursor = conn.cursor()

columns = [
    ("poster_path", "TEXT"),
    ("overview", "TEXT"),
    ("tmdb_id", "INTEGER"),
    ("popularity", "REAL"),
    ("trailer_key", "TEXT")
]

for column, dtype in columns:

    try:
        cursor.execute(
            f"ALTER TABLE movies ADD COLUMN {column} {dtype}"
        )
        print(f"Added {column}")

    except sqlite3.OperationalError:
        print(f"{column} already exists")

conn.commit()
conn.close()

print("Schema Updated.")