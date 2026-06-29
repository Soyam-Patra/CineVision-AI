from fastapi import APIRouter, HTTPException
from app.services.recommendation_service import recommend_movies
router = APIRouter()

@router.get("/movies/{actor}")
def get_movies(actor: str):

    movies = recommend_movies(actor)

    if not movies:
        raise HTTPException(
            status_code=404,
            detail="Actor not found or no movies available."
        )

    return {
        "actor": actor,
        "count": len(movies),
        "movies": movies
    }