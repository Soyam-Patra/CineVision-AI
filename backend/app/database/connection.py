from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[2]

print(ROOT)
DB_PATH = ROOT / "movies.db"
print(DB_PATH)

conn = sqlite3.connect(
    DB_PATH,
    check_same_thread=False
)

cursor = conn.cursor()