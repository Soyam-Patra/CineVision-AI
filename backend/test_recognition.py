import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from app.recognition.faiss_index import recognize

from app.recognition.faiss_index import recognize

results = recognize("backend/test.jpg")

for r in results:
    print(r)

from app.database.connection import cursor

cursor.execute("""
SELECT movie_title, poster_path
FROM movies
WHERE movie_title=?
""", ("Pirates of the Caribbean: The Curse of the Black Pearl",))

print(cursor.fetchone())