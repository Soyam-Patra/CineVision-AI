from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[2]

conn = sqlite3.connect(
    ROOT / "movies.db",
    check_same_thread=False
)

cursor = conn.cursor()