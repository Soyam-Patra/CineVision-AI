from collections import defaultdict

from app.recognition.faiss_index import recognize
from app.services.recommendation_service import recommend_movies

CONFIDENCE_THRESHOLD = 0.60



def predict_actor(image_path):

    faces = recognize(image_path)

    if not faces:

        return {
            "success": False,
            "message": "No face detected in the image."
        }

    predictions = []

    for face in faces:

        results = face["matches"]

        if not results:
            continue

        best = results[0]

        if best["score"] < CONFIDENCE_THRESHOLD:
            continue

        actor_scores = defaultdict(float)

        for result in results:

            actor_scores[result["actor"]] += result["score"]

        actor = max(
            actor_scores,
            key=actor_scores.get
        )

        movies = recommend_movies(actor)

        predictions.append({

            "actor": actor,

            "confidence": round(best["score"] * 100, 2),

            "weighted_score": round(actor_scores[actor], 3),

            "matches": len(results),

            "bbox": best["bbox"],

            "movies": movies

        })

    if len(predictions) == 0:

        return {

            "success": False,

            "message": "No recognizable actors found."

        }

    return {

        "success": True,

        "num_faces": len(predictions),

        "actors": predictions

    }