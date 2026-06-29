from pathlib import Path
import numpy as np
import faiss

ROOT = Path(__file__).resolve().parents[2]

EMBEDDING_DIR = ROOT / "backend" / "actor_database" / "embeddings"

embeddings = np.load(EMBEDDING_DIR / "embeddings.npy").astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

index.add(embeddings)

faiss.write_index(
    index,
    str(EMBEDDING_DIR / "actor_index.faiss")
)

print(f"Dimension : {dimension}")
print(f"Embeddings : {index.ntotal}")
print("FAISS index saved.")