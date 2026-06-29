from pathlib import Path
import cv2
import faiss
import numpy as np
import pickle

from insightface.app import FaceAnalysis

ROOT = Path(__file__).resolve().parents[2]

EMBEDDING_DIR = ROOT / "actor_database" / "embeddings"

# ---------- Load FAISS ---------- #

index = faiss.read_index(
    str(EMBEDDING_DIR / "actor_index.faiss")
)

# ---------- Load Metadata ---------- #

with open(
    EMBEDDING_DIR / "metadata.pkl",
    "rb"
) as f:

    metadata = pickle.load(f)

# ---------- Load InsightFace ---------- #

app = FaceAnalysis(name="buffalo_l")

app.prepare(
    ctx_id=0,
    det_size=(640,640)
)

# ---------- Search ---------- #

def recognize(image_path, top_k=5):

    image = cv2.imread(str(image_path))

    faces = app.get(image)

    if len(faces) == 0:

        return []

    all_results = []

    for face in faces:

        embedding = face.embedding

        embedding = embedding / np.linalg.norm(embedding)

        embedding = embedding.astype("float32").reshape(1, -1)

        scores, indices = index.search(
            embedding,
            top_k
        )

        results = []

        for score, idx in zip(scores[0], indices[0]):

            results.append(
                {
                    "actor": metadata[idx]["actor_name"],
                    "score": float(score),

                    "bbox": [
                        int(face.bbox[0]),
                        int(face.bbox[1]),
                        int(face.bbox[2]),
                        int(face.bbox[3])
                    ]
                }
            )

        all_results.append({

            "bbox": face.bbox.tolist(),

            "matches": results

        })

    return all_results