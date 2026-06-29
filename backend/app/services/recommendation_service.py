from app.database.connection import cursor


def recommend_movies(actor_name, limit=10):

    cursor.execute(
        """
        SELECT
            movie_title,
            imdb_score,
            genres,
            title_year,
            duration,
            poster_path,
            overview,
            trailer_key,
            popularity,
            tmdb_rating,
            tmdb_vote_count
        FROM movies
        WHERE
            actor_1_name=?
            OR actor_2_name=?
            OR actor_3_name=?
        ORDER BY imdb_score DESC
        LIMIT ?
        """,
        (
            actor_name,
            actor_name,
            actor_name,
            limit
        )
    )

    rows = cursor.fetchall()

    movies = []

    for row in rows:

        BASE_POSTER = "https://image.tmdb.org/t/p/w500"
        BASE_TRAILER = "https://www.youtube.com/watch?v="

        movies.append(
            {
                "title": row[0].strip(),
                "imdb_rating": row[1],
                "genres": row[2].split("|"),
                "year": int(row[3]) if row[3] else None,
                "runtime": int(row[4]) if row[4] else None,

                "poster": (
                    BASE_POSTER + row[5]
                    if row[5]
                    else None
                ),

                "overview": row[6],

                "trailer": (
                    BASE_TRAILER + row[7]
                    if row[7]
                    else None
                ),

                "popularity": row[8],
                "tmdb_rating": row[9],
                "tmdb_votes": row[10]
            }
        
        )
        print(row)

    return movies