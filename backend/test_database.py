from app.services.recommendation_service import recommend_movies

movies = recommend_movies("Johnny Depp")

for movie in movies:
    print(movie)
from app.database.connection import cursor



cursor.execute("""
SELECT
movie_title,
poster_path,
overview,
tmdb_id
FROM movies
WHERE movie_title LIKE '%Pirates%'
""")

for row in cursor.fetchall():
    print(row)



'''cursor.execute("""
SELECT
    movie_title,
    poster_path,
    overview,
    tmdb_rating,
    tmdb_vote_count,
    trailer_key
FROM movies
WHERE movie_title LIKE '%Curse of the Black Pearl%'
""")

print(cursor.fetchone())'''