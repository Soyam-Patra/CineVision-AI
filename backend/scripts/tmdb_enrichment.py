from pathlib import Path
import sqlite3
import requests
import time

API_KEY = "67b561e775bf974e7893e5f76d5dd81a"

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "backend" / "movies.db"
print(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

#reading movies
cursor.execute("""
SELECT DISTINCT
    rowid,
    movie_title,
    title_year
FROM movies
WHERE
    poster_path IS NULL               
""")

movies = cursor.fetchall()

print(f"Movies to enrich: {len(movies)}")


#Search tmdb
SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

for rowid, title, year in movies:

    title = title.strip()

    params = {
        "api_key": API_KEY,
        "query": title,
        "year": int(year) if year else None
    }

    response = requests.get(
        SEARCH_URL,
        params=params,
        timeout=20
    )

    if response.status_code != 200:
        print(f"{title}")
        print("Status:", response.status_code)
        print(response.text)
        continue

    results = response.json()["results"]

    if not results:
        print("Not found:", title)
        continue

    movie = results[0]
    print("\n----------------------------")
    print("Dataset Title :", title)
    print("TMDb Title    :", movie["title"])
    print("TMDb ID       :", movie["id"])
    print("Release Date  :", movie.get("release_date"))
    print("----------------------------")

#Get movie data
    movie_id = movie["id"]

    details = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}",
        params={"api_key": API_KEY}
    ).json()

    print("Poster:", details.get("poster_path"))
    print("Overview exists:", details.get("overview") is not None)


    #For TRailer
    videos = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}/videos",
        params={"api_key": API_KEY}
    ).json()

    trailer = None

    for video in videos.get("results", []):

        if (
            video["site"] == "YouTube"
            and video["type"] == "Trailer"
        ):
            trailer = video["key"]
            break 


    cursor.execute(
        """
        UPDATE movies
        SET
            tmdb_id=?,
            poster_path=?,
            backdrop_path=?,
            overview=?,
            popularity=?,
            tmdb_rating=?,
            tmdb_vote_count=?,
            trailer_key=?
        WHERE rowid=?
        """,
        (
            movie_id,
            details.get("poster_path"),
            details.get("backdrop_path"),
            details.get("overview"),
            details.get("popularity"),
            details.get("vote_average"),
            details.get("vote_count"),
            trailer,
            rowid
        )
    )

    conn.commit()

    print("Updated:", title)

    time.sleep(0.25)

#closing connection  
conn.close()

print("Finished enrichment.")