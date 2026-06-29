from pathlib import Path
import cv2
import numpy as np
import pickle
import faiss
import pandas as pd

from tqdm import tqdm
from insightface.app import FaceAnalysis

# ---------------- CONFIG ---------------- #

ROOT = Path(__file__).resolve().parents[2]

IMAGE_DIR = ROOT / "backend" / "actor_database" / "actor_images"

EMBEDDING_DIR = ROOT / "backend" / "actor_database" / "embeddings"

EMBEDDING_DIR.mkdir(parents=True, exist_ok=True)

# ---------------- InsightFace ---------------- #

app = FaceAnalysis(name="buffalo_l")

app.prepare(
    ctx_id=0,
    #providers=["CUDAExecutionProvider", "CPUExecutionProvider"],
    det_size=(640, 640)
)

# ---------------- Actor Lookup ---------------- #

actors_df = pd.read_csv(
    ROOT / "backend" / "actor_database" / "actors.csv"
)

actor_lookup = dict(
    zip(
        actors_df.actor_id,
        actors_df.actor_name
    )
)

# ---------------- Storage ---------------- #

all_embeddings = []
metadata = []

actor_folders = sorted(IMAGE_DIR.iterdir())

# ---------------- Statistics ---------------- #

processed = 0
no_face = 0
multi_face = 0
invalid_image = 0

# ---------------- Generate Embeddings ---------------- #

for folder in tqdm(actor_folders, desc="Generating Embeddings"):

    if not folder.is_dir():
        continue

    actor_id = int(folder.name)

    for image_path in folder.glob("*.jpg"):

        image = cv2.imread(str(image_path))

        if image is None:

            invalid_image += 1

            continue

        faces = app.get(image)

        if len(faces) == 0:

            no_face += 1

            continue

        if len(faces) > 1:

            multi_face += 1

        # Choose the largest detected face

        face = max(
            faces,
            key=lambda f: (
                (f.bbox[2] - f.bbox[0]) *
                (f.bbox[3] - f.bbox[1])
            )
        )

        embedding = face.embedding

        embedding = embedding / np.linalg.norm(embedding)

        embedding = embedding.astype(np.float32)

        all_embeddings.append(embedding)

        metadata.append(
            {
                "embedding_index": len(all_embeddings),
                "actor_id": actor_id,
                "actor_name": actor_lookup.get(
                    actor_id,
                    "Unknown"
                ),
                "image": image_path.name
            }
        )

        processed += 1

# ---------------- Convert ---------------- #

all_embeddings = np.asarray(
    all_embeddings,
    dtype=np.float32
)

# ---------------- Save Embeddings ---------------- #

np.save(
    EMBEDDING_DIR / "embeddings.npy",
    all_embeddings
)

with open(
    EMBEDDING_DIR / "metadata.pkl",
    "wb"
) as f:

    pickle.dump(metadata, f)

# ---------------- Build FAISS ---------------- #

dimension = all_embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

index.add(all_embeddings)

faiss.write_index(
    index,
    str(EMBEDDING_DIR / "actor_index.faiss")
)

# ---------------- Summary ---------------- #

print("\n" + "=" * 40)

print("Embedding Generation Complete")

print("=" * 40)

print(f"Actors Processed      : {len(actor_folders)}")
print(f"Embeddings Generated  : {processed}")
print(f"No Face Images        : {no_face}")
print(f"Multi Face Images     : {multi_face}")
print(f"Invalid Images        : {invalid_image}")

print("\nSaved Files")

print("embeddings.npy")
print("metadata.pkl")
print("actor_index.faiss")

print("=" * 40)