from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
BACKEND_ROOT = PROJECT_ROOT / "backend"

MOVIES_DB = BACKEND_ROOT / "movies.db"
ACTOR_DATABASE = BACKEND_ROOT / "actor_database"
EMBEDDINGS = ACTOR_DATABASE / "embeddings"
ACTOR_IMAGES = ACTOR_DATABASE / "actor_images"