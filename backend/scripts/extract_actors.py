import pandas as pd
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]

df = pd.read_csv(ROOT / "data" / "movie_metadata.csv")

actors = []

for col in ["actor_1_name", "actor_2_name", "actor_3_name"]:
    actors.extend(df[col].dropna().tolist())

actor_counts = (
    pd.Series(actors)
    .value_counts()
    .reset_index()
)

actor_counts.columns = ["actor_name", "movie_count"]

actor_counts["actor_id"] = range(1, len(actor_counts) + 1)


def get_tier(count):
    if count >= 20:
        return 1
    elif count >= 8:
        return 2
    elif count >= 3:
        return 3
    else:
        return 4


actor_counts["tier"] = actor_counts["movie_count"].apply(get_tier)

# Create artifacts folder
OUTPUT_DIR = ROOT / "backend" / "actor_database"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

actor_counts.to_csv(OUTPUT_DIR / "actors.csv", index=False)

print(actor_counts.head())
print(f"\nSaved {len(actor_counts)} actors.")