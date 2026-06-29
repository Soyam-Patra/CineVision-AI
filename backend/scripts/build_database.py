from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

ROOT = Path(__file__).resolve().parents[2]

csv_path = ROOT / "data" / "movie_metadata.csv"

db_path = ROOT / "backend" / "movies.db"

df = pd.read_csv(csv_path)

df["tmdb_id"] = None
df["poster_path"] = None
df["backdrop_path"] = None
df["overview"] = None
df["popularity"] = None
df["tmdb_rating"] = None
df["tmdb_vote_count"] = None
df["trailer_key"] = None

engine = create_engine(f"sqlite:///{db_path}")

df.to_sql(
    "movies",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully!")
print(f"Movies: {len(df)}")